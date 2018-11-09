from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.extensions.email_server import send_email_code
from app.models import User


class Email(APIView):
    def post(self, requset):
        if type(requset.user)=='AnonymousUser':
            send_email_code(requset.user.email)
            return Response({'message': 'send email successfully'}, status=status.HTTP_200_OK)
        else:
            email = requset.data['email']
            if email:
                if User.objects.filter(email=email):
                    send_email_code(email)
                    return Response({'message': 'send email sucessfully'}, status=status.HTTP_200_OK)
                return Response({'message': 'email is required'}, status=status.HTTP_402_PAYMENT_REQUIRED)
