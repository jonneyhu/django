from app.utils import Base,Manager
from django.db import models

class Notification(Base):
    object=Manager()
    operate = models.IntegerField( nullable=False)
    is_sms_active = models.BooleanField( nullable=False, default=False)
    is_mail_active = models.BooleanField( nullable=False, default=False)
    profile_id = models.ForeignKey("Profile")