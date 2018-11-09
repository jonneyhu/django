from app.util import Base,Manager
from django.db import models
class AdminRole(Base):
    objects=Manager()
    users = models.ForeignKey('User', on_delete=models.CASCADE,related_name='adminrole')
    role_name = models.CharField(max_length=50)
    role_description = models.CharField(max_length=100)
    authority = models.CharField(max_length=100)


