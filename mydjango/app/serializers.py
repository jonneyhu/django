from django.contrib.auth.models import User,Group
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from app.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet, Book, Auth


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields=('url','name')

class UserSerializer(serializers.ModelSerializer):
    # groups=GroupSerializer()
    class Meta:
        model=User
        fields=('url','username','email','groups')

class BookSerializer(serializers.ModelSerializer):
    # auth=PrimaryKeyRelatedField(queryset=Auth.objects.all())
    class Meta:
        model=Book
        fields=('name','title','auth')

class AuthSerializer(serializers.ModelSerializer):
    # book=BookSerializer()
    class Meta:
        model=Auth
        fields=('name','age','sex','say','book')



class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    lineonos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        根据提供的验证过的数据创建并返回一个新的`Snippet`实例。
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        根据提供的验证过的数据更新和返回一个已经存在的`Snippet`实例。
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.lineonos = validated_data.get('lineonos', instance.lineonos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
    # class Meta:
    #     model=Snippet
    #     fields=('id', 'title', 'code', 'linenos', 'language', 'style')