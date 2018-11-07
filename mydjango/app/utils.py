from datetime import timezone
from django.db import models
class Base(models.Model):
    created_at=models.DateTimeField('创建时间',auto_now_add=True)
    updated_at=models.DateTimeField('更新时间',auto_now=True)
    deleted_at=models.DateTimeField('删除时间',null=True,default=None)
    def delete(self,using=None,keep_parents=False):
        self.deleted_at=timezone.now()
        self.save()
    class Meta:
        abstract=True


class Manager(models.Manager):
    def get_queryset(self):
        return super(Manager, self).get_queryset().filter(deleted_at=None)