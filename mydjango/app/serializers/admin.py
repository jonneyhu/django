from rest_framework import serializers

from app.models import User


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','data_joined','role_type',)