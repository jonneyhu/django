from datetime import datetime, timedelta

from django.db.models import Q, Sum

from app.const import DepositOrWithdrawStatus, Config
from app.util import Base, Manager
from django.db import models


class Withdraw(Base):
    objects = Manager()
    user_profile = models.ForeignKey('Profile', on_delete=models.PROTECT)
    amount = models.BigIntegerField(default=0)
    actual_amount = models.BigIntegerField(default=0)
    bank_txid = models.CharField(max_length=80)
    blcokchain_txid = models.CharField(max_length=80)
    redeem_txid = models.CharField(max_length=80)
    status = models.IntegerField(
        default=DepositOrWithdrawStatus.submitting.value)
    currency = models.CharField(max_length=80, default=Config.CURRENCY)

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
    @staticmethod
    def get_withdraw_by_user(user_id):
        return Withdraw.objects.filter(user_profile__users__id=user_id)
    @staticmethod
    def get_withdraw_by_type(search, type):
        if search:
            if search.isnumeric():
                search_filter = Q(user_profile__users__id=int(search))
            else:
                search_filter = Q(user_profile__users__username=search)
        else:
            search_filter = ~Q(id=0)

        if int(type) == 0:

            return Withdraw.objects.filter(search_filter, Q(created_at__gte=datetime.now() - timedelta(days=14)) \
                                    , Q(status=DepositOrWithdrawStatus.submitting.value) | Q(status =\
                                    DepositOrWithdrawStatus.accepted.value)).order_by('-id')

        if int(type) == 1:
            return Withdraw.objects.filter(search_filter, ~Q(status=DepositOrWithdrawStatus.submitting.value),
                                    ~Q(status=DepositOrWithdrawStatus.accepted.value)).order_by('-id')
        else:
            return Withdraw.objects.filter(search_filter, Q(created_at__lte=datetime.now() - timedelta(days=14)),
                                    Q(status=DepositOrWithdrawStatus.submitting.value)).order_by('-id')
    @staticmethod
    def get_today_withdraw(user_id):
        today=datetime.today()
        zero_time=datetime(today.year,today.month,today.day,0,0,0,0)
        withdraw_sum=Withdraw.objects.annotate(withdraw_sum=Sum('amount')).filter(created_at__gte=zero_time,user_profile__users__id=user_id)
        return withdraw_sum

    def is_exsit_txid(self,txid):
        return Withdraw.objects.filter(blcokchain_txid=txid)
    def is_exsit_bank_txid(self,bank_txid):
        return Withdraw.objects.filter(bank_txid=bank_txid)


