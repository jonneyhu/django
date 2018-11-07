
from app.utils import Base,Manager
from django.db import models
class Fee(Base):
    objects=Manager()
    withdraw_id=models.OneToOneField('Withdraw',on_delete=models.CASCADE,related_name='fee')
    amount=models.BigIntegerField(null=False)
