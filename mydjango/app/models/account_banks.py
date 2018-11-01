from app.utils import Base,Manager
from django.db import models

class AccountBank(Base):
    object=Manager()
    label=models.CharField(max_length=80)
    bsb=models.CharField(max_length=80)
    account_number=models.CharField(max_length=80)
    bank_name=models.CharField(max_length=100)
    account_name=models.CharField(max_length=80)
    swift=models.CharField(max_length=100)
    beneficiary_address=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    user_id=models.ForeignKey('User',on_delete=False)


