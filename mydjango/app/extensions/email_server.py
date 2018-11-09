from .redis_server import  generate_email_code, get_email_info, del_email_code
from celery_tasks.email.tasks import send_mail_code

def send_email_code(email):
    code=generate_email_code(email)
    send_mail_code.delay(email,str(code))
def check_email_code(code,email,deleted=True):
    mail_code=get_email_info(email)
    if mail_code == int(code):
        if deleted:
            del_email_code(email)
        return True
    else:
        return False