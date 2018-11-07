from django.conf import settings
from django.core.mail import send_mail
from app.celery_tasks.main import app


@app.task(name='send_mail_code')
def send_mail(to,message):
    send_mail('邮箱验证',html_message=message,from_email=settings.EMAIL_FROM,to=[to])
