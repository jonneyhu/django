from app.utils import Base,Manager
from django.db import models


class AccountTranssction(Base):
    object=Manager()

    tx_id = models.CharField(max_length=80)
    tx_from =models.CharField(max_length=70)
    tx_to = models.CharField(max_length=70)
    amount = models.BigIntegerField()
    date = models.DateTimeField()