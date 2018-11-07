from .redis_server import  generate_email_code, get_email_info, del_email_code
from app.celery_tasks.email.email import send_mail
def send_email_code(email):
    code=generate_email_code()
    send_mail.delay(email,code)
def check_email_code(code,email,deleted=True):
    mail_code=get_email_info(email)
    if mail_code == int(code):
        if deleted:
            del_email_code(email)
        return True
    else:
        return False