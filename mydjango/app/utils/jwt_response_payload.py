import re

from django.contrib.auth.backends import ModelBackend

from app.models import User


def jwt_response_payload_handler(token,user=None,request=None):
    return {
        'token': token,
        'username': user.username,
        'id': user.id
    }

class UserLoginBackend(ModelBackend):
    def authenticate(self,request,username=None,password=None,**kwargs):
        try:
            if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',username):
                user=User.objects.get(email=username)
            else:
                user=User.objects.get(username=username)
        except:
            user=None
        if user is not None and user.check_password(password):
            return user



