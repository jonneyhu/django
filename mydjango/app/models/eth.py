from app.util import Base,Manager
from django.db import models
class Eth(Base):
    objects=Manager()
    eth_label = models.CharField(max_length=80, null=True)
    eth_address = models.CharField(max_length=80, null=True)
    profile_id= models.ForeignKey('Profile',on_delete=models.CASCADE)

