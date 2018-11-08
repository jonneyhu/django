from app.util import Base,Manager
from django.db import models
class UserKyc(Base):
    objects=Manager()
    users = models.OneToOneField('User', on_delete=models.CASCADE,related_name='userkyc')
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

