from django.conf import settings
from django.core.mail import send_mail
from celery_tasks.main import app


@app.task(name='send_mail_code')
def send_mail_code(to,message):
    send_mail('邮箱验证',message,settings.EMAIL_FROM,[to])
