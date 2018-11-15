from rest_framework import serializers, status
from rest_framework.response import Response

from app.models import Withdraw


class WithdrawList(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(read_only=True,default=serializers.CurrentUserDefault())
    class Meta:
        model=Withdraw
        fields=('id','amount','user','created_at','updated_at','actual_amount')
        read_only_fields=('created_at','updated_at','actual_amount')
        depth=1
    # def create(self, validated_data):
    #     validated_data['user_profile']=self.context['request'].user.profile
    #     withdraw=Withdraw.objects.create(**validated_data)
    #     return withdraw
