from app.utils import Base,Manager
from django.db import models
class AccountBank(Base):
    objects=Manager()
    users = models.OneToOneField('User', on_delete=models.CASCADE,related_name='accountbank',verbose_name='用户')
    label=models.CharField(max_length=80,verbose_name='标签')
    bsb=models.CharField(max_length=80)
    account_number=models.CharField(max_length=80)
    bank_name=models.CharField(max_length=100)
    account_name=models.CharField(max_length=80)
    swift=models.CharField(max_length=100)
    beneficiary_address=models.CharField(max_length=255)
    address=models.CharField(max_length=255)

