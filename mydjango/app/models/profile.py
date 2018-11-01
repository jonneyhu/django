from app.utils import Base,Manager
from django.db import models

class Profile(Base):
    object=Manager()
    user_id = models.OneToOneField('User')
    phone = models.CharField(max_length=20)
    status = models.IntegerField()
    KYC_status = models.IntegerField( default=UserKycType.no_submit.value)
    KYC_reason = models.CharField(max_length=80)
    avatar = models.TextField( nullable=True, default=None)
    is_binding_google = models.BooleanField(default=False)
    is_binding_sms = models.BooleanField( default=False)
    google_secret_key = models.CharField(max_length=80)
    eth_label = models.CharField(max_length=80, nullable=True)
    eth_address = models.CharField(max_length=80, nullable=True)
    current_amount = models.BigIntegerField()
    frozen = models.BigIntegerField()
