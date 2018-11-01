from app.utils import Base,Manager
from django.db import models
from app.const import Config
class Deposit(Base):
    object=Manager()
    amount = models.BigIntegerField()
    actual_amount = models.BigIntegerField(default=0)
    bank_txid = models.CharField(max_length=80)
    blcokchain_txid = models.CharField(max_length=80)
    issue_txid = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    order = models.CharField(max_length=16)
    status = models.IntegerField(
        default=DepositOrWithdrawStatus.submitting.value)
    currency = models.CharField(max_length=80, default=Config.CURRENCY)
    profile_id = models.ForeignKey("user_profiles")