from app.util import Base,Manager
from django.db import models
class Notification(Base):
    objects=Manager()
    operate = models.IntegerField( null=False)
    is_sms_active = models.BooleanField( null=False, default=False)
    is_mail_active = models.BooleanField( null=False, default=False)
    profile_id = models.ForeignKey("Profile",on_delete=models.CASCADE)
