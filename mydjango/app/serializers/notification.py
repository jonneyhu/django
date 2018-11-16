from rest_framework import serializers

from app.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields= ('operate','is_sms_active','is_mail_active')

