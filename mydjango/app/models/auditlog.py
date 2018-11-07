from app.utils import Base,Manager
from django.db import models
class AuditLog(Base):
    objects=Manager()
    operate_id = models.IntegerField()
    operate_email = models.CharField(max_length=80)
    type = models.IntegerField()
    actions = models.TextField()