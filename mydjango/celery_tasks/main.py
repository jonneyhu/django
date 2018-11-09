from celery import Celery
import os

if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE']='mydjango.settings'
# 创建应用
app=Celery('mydjango')
# 导入配置
app.config_from_object('celery_tasks.config')
# 自动添加任务
app.autodiscover_tasks(['celery_tasks.sms','celery_tasks.email','celery_tasks.wallet'])

#启动
#  celery -A celery_tasks.main worker -l info
