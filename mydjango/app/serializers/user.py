import re

from rest_framework import serializers, status
from rest_framework.response import Response

from app.extensions.email_server import check_email_code
from app.models import User, UserKyc, Profile
from itsdangerous import TimedJSONWebSignatureSerializer as jwt
from rest_framework_jwt.settings import api_settings


class CreateUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=20, min_length=8, write_only=True)
    email_code = serializers.CharField(max_length=6, min_length=6, write_only=True)
    # allow = serializers.CharField(write_only=True)

    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password2', 'email', 'token', 'email_code')

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
        if not check_email_code(attrs['email_code'], attrs['email'], deleted=False):
            raise serializers.ValidationError('email verification failed')
        return attrs

    def create(self, validated_data):

        del validated_data['password2']
        del validated_data['email_code']
        # del validated_data['allow']

        user = super().create(validated_data)

        # 密码加密
        user.set_password(validated_data['password'])
        user.save()
        userprofile = Profile(users_id=user.id)
        userprofile.save()
        userkyc = UserKyc(users_id=user.id)
        userkyc.save()
        # 生成jwtoken值
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        # 对用户对象添加额外属性
        user.token = token
        return user

    def update(self, instance, validated_data):
        if instance:
            if not check_email_code(validated_data['code'], validated_data['email'], deleted=False):
                return Response({'message': 'code is wrong'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                del validated_data['code']
                del validated_data['email']
                instance.set_password(validated_data['password'])
                instance.save()
                return Response({'message': 'update successfully'}, status=status.HTTP_205_RESET_CONTENT)
        return Response({'message': 'email not exsits'}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailSerializer(serializers.ModelSerializer):
    newpassword = serializers.CharField(max_length=20, min_length=8, write_only=True)

    class Meta:
        model = User
        exclude = ('password',)
        depth = 2
        extra_kwargs = {
            'password': {'write_only': True,
                         'min_length': 8,
                         'max_length': 20,
                         'error_messages': {
                             'min_length': '仅允许8-20个字符的密码',
                             'max_length': '仅允许8-20个字符的密码',
                         }
                         }
        }

    def update(self, instance, validated_data):
        if instance.check_password(validated_data['password']):
            instance.set_password(validated_data['newpassword'])
            return instance
        return Response({'message': 'password is wrong'}, status=status.HTTP_406_NOT_ACCEPTABLE)
