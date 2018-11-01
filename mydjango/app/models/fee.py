from app.utils import Base,Manager
from django.db import models

class Fee(Base):
    object=Manager()
    withdraw=models.ForeignKey('Withdraw')
    amount=models.BigIntegerField(null=False)
