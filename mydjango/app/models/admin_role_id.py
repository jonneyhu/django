from app.utils import Base,Manager
from django.db import models
class AdminRole(Base):
    object=Manager()
    role_name = models.CharField(max_length=50)
    role_description = models.CharField(max_length=100)
    authority = models.CharField(max_length=100)