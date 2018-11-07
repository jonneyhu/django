from app.const import DepositOrWithdrawStatus, Config
from app.utils import Base,Manager
from django.db import models
class Withdraw(Base):
    objects=Manager()
    user_profile = models.ForeignKey('Profile',on_delete=models.PROTECT)
    amount = models.BigIntegerField()
    actual_amount = models.BigIntegerField( default=0)
    bank_txid = models.CharField(max_length=80)
    blcokchain_txid = models.CharField(max_length=80)
    redeem_txid = models.CharField(max_length=80)
    status = models.IntegerField(
        default=DepositOrWithdrawStatus.submitting.value)
    currency =models.CharField(max_length=80, default=Config.CURRENCY)

    bank_label = models.CharField(max_length=80)
    bank_bsb = models.CharField(max_length=80)
    bank_account_number = models.CharField(max_length=80)
    bank_bank_name = models.CharField(max_length=100)
    bank_account_name = models.CharField(max_length=80)
    bank_swift = models.CharField(max_length=100)
    bank_beneficiary_address = models.CharField(max_length=255)
    bank_address = models.CharField(max_length=255)

    remark = models.TextField()
    address = models.CharField(max_length=80)
