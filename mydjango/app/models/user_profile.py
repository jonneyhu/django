from app.const import UserKycType
from app.models import Notification
from app.util import Base, Manager
from django.db import models


class Profile(Base):
    objects = Manager()
    users = models.OneToOneField('User', on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20)
    status = models.IntegerField(default=0)
    KYC_status = models.IntegerField(default=UserKycType.no_submit.value)
    KYC_reason = models.CharField(max_length=80)
    avatar = models.TextField(null=True, default=None)
    is_binding_google = models.BooleanField(default=False)
    is_binding_sms = models.BooleanField(default=False)
    google_secret_key = models.CharField(max_length=80)
    current_amount = models.BigIntegerField(default=0)
    frozen = models.BigIntegerField(default=0)

    def is_login_notification(self):
        noftifications = self.notification_set.all()
        for n in noftifications:
            if n.operate == 0:
                return n.is_sms_active, n.is_mail_active
        return False, False

    def is_withdraw_notification(self):
        noftifications = self.notification_set.all()
        for n in noftifications:
            if n.operate == 1:
                return n.is_sms_active, n.is_mail_active
        return False, False

    def is_deposit_notification(self):
        notifications = self.notification_set.all()
        for n in notifications:
            if n.operate == 2:
                return n.is_sms_active, n.is_mail_active
        return False, False
