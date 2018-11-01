from app.utils import Base,Manager
from django.db import models
class User(Base):
    object=Manager()
    username= models.CharField(max_length=80,unique=True,null=False)
    email=models.EmailField(max_length=80,unique=True,null=False)
    password_hash=models.CharField(max_length=255,null=False)
    role_type=models.IntegerField(null=False,default=0)
    is_active=models.BooleanField(null=False,default=False)
    is_id_verified=models.BooleanField(null=False,default=False)
    admin_role_id=models.ForeignKey('AdminRole')
    profile=models.OneToOneField('Profile')
    userkyc=models.OneToOneField('UserKyc')
    account_banks= models.OneToOneField('AccountBank')



















