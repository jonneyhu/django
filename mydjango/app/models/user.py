from app.utils import Base,Manager
from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    role_type=models.IntegerField(null=False,default=0,verbose_name='角色类型')
    is_active=models.BooleanField(null=False,default=False,verbose_name='是否激活')
    is_id_verified=models.BooleanField(null=False,default=False,verbose_name='身份是否验证')
    class Meta:
        db_table='users'
        verbose_name='用户'
        verbose_name_plural=verbose_name