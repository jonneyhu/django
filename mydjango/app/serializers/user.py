import re

from rest_framework import serializers

from app.extensions.email_server import check_email_code
from app.models import User
from itsdangerous import TimedJSONWebSignatureSerializer as jwt
from rest_framework_jwt.settings import api_settings


class CreateUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=20, min_length=8, write_only=True)
    # sms_code = serializers.CharField(max_length=6, min_length=6, write_only=True)
    # allow = serializers.CharField(write_only=True)

    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password2', 'email', 'token')

        extra_kwargs = {
            'username': {
                'max_length': 20,
                'min_length': 5,
                'error_messages': {
                    'max_length': '名字太长',
                    'min_length': '名字太短'
                }
            },
            'password': {
                'write_only': True,
                'min_length': 8,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许8-20个字符的密码',
                    'max_length': '仅允许8-20个字符的密码',
                }
            }
        }

    # 手机号验证
    def validate_email(self, value):

        rx = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        if not rx.search(value):
            raise serializers.ValidationError('email is wrong')
        return value
    # 多个数据验证
    def validate(self, attrs):

        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('两次密码不一致')

        # # 短信验证码验证
        # conn = get_redis_connection('verify_codes')
        #
        # real_sms_code = conn.get('sms_code_%s' % attrs['mobile'])
        #
        # if not real_sms_code:
        #     raise serializers.ValidationError('验证码已失效')
        #
        # if attrs['sms_code'] != real_sms_code.decode():
        #     raise serializers.ValidationError('验证码不一致')

        return attrs

    def create(self, validated_data):

        del validated_data['password2']
        # del validated_data['sms_code']
        # del validated_data['allow']

        user = super().create(validated_data)

        # 密码加密
        user.set_password(validated_data['password'])
        user.save()

        # 生成jwtoken值

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        # 对用户对象添加额外属性
        user.token = token

        return user
class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        exclude=('password',)
        depth=2