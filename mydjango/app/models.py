from app.const import DepositOrWithdrawStatus, Config, UserKycType
from app.utils import Base,Manager
from django.db import models
class AdminRole(Base):
    object=Manager()
    users = models.ForeignKey('User', on_delete=models.CASCADE,related_name='adminrole')
    role_name = models.CharField(max_length=50)
    role_description = models.CharField(max_length=100)
    authority = models.CharField(max_length=100)
class User(Base):
    object=Manager()
    username= models.CharField(max_length=80,unique=True,null=False)
    email=models.EmailField(max_length=80,unique=True,null=False)
    password_hash=models.CharField(max_length=255,null=False)
    role_type=models.IntegerField(null=False,default=0)
    is_active=models.BooleanField(null=False,default=False)
    is_id_verified=models.BooleanField(null=False,default=False)

class Profile(Base):
    object=Manager()
    users = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
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


class UserKyc(Base):
    object=Manager()
    users = models.OneToOneField(User, on_delete=models.CASCADE,related_name='userkyc')
    given_name = models.CharField(max_length=80)
    family_name = models.CharField(max_length=80)
    birthday =models.DateTimeField()
    kyc_file_type = models.CharField(max_length=80)
    id_document_type = models.CharField(max_length=80)
    file_number = models.CharField(max_length=80)
    expire_date = models.DateTimeField()
    kyc_file = models.TextField()
    document_file = models.TextField()
    country = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    zip_code = models.CharField(max_length=80)
    address = models.CharField(max_length=80)



class Withdraw(Base):
    object=Manager()
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
    profile_id = models.ForeignKey("Profile",on_delete=models.PROTECT,related_name='deposit')

class Notification(Base):
    object=Manager()
    operate = models.IntegerField( null=False)
    is_sms_active = models.BooleanField( null=False, default=False)
    is_mail_active = models.BooleanField( null=False, default=False)
    profile_id = models.ForeignKey("Profile",on_delete=models.CASCADE)


class Fee(Base):
    object=Manager()
    withdraw_id=models.OneToOneField('Withdraw',on_delete=models.CASCADE,related_name='fee')
    amount=models.BigIntegerField(null=False)

class Eth(Base):
    object=Manager()
    eth_label = models.CharField(max_length=80, null=True)
    eth_address = models.CharField(max_length=80, null=True)
    profile_id= models.ForeignKey('Profile',on_delete=models.CASCADE)

class AccountBank(Base):
    object=Manager()
    users = models.OneToOneField(User, on_delete=models.CASCADE,related_name='accountbank')
    label=models.CharField(max_length=80)
    bsb=models.CharField(max_length=80)
    account_number=models.CharField(max_length=80)
    bank_name=models.CharField(max_length=100)
    account_name=models.CharField(max_length=80)
    swift=models.CharField(max_length=100)
    beneficiary_address=models.CharField(max_length=255)
    address=models.CharField(max_length=255)



class AccountTranssction(Base):
    object=Manager()
    tx_id = models.CharField(max_length=80)
    tx_from =models.CharField(max_length=70)
    tx_to = models.CharField(max_length=70)
    amount = models.BigIntegerField()
    date = models.DateTimeField()




class AuditLog(Base):
    object=Manager()
    operate_id = models.IntegerField()
    operate_email = models.CharField(max_length=80)
    type = models.IntegerField()
    actions = models.TextField()