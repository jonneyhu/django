from app.const import UserKycType
from app.util import Base,Manager
from django.db import models
class Profile(Base):
    objects=Manager()
    users = models.OneToOneField('User', on_delete=models.CASCADE,related_name='profile')
    phone = models.CharField(max_length=20)
    status = models.IntegerField()
    KYC_status = models.IntegerField( default=UserKycType.no_submit.value)
    KYC_reason = models.CharField(max_length=80)
    avatar = models.TextField( null=True, default=None)
    is_binding_google = models.BooleanField(default=False)
    is_binding_sms = models.BooleanField( default=False)
    google_secret_key = models.CharField(max_length=80)
    current_amount = models.BigIntegerField()
    frozen = models.BigIntegerField()