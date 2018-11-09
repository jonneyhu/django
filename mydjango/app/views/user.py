from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework_jwt.views import ObtainJSONWebToken
from app.extensions.email_server import check_email_code
from app.models import User
from app.serializers.user import CreateUserSerializer, UserDetailSerializer
from rest_framework import status


class UserView(CreateAPIView):
    serializer_class = CreateUserSerializer


class UserDetail(RetrieveAPIView,UpdateAPIView):
    serializer_class = UserDetailSerializer
    permissions = [IsAuthenticated]
    def get_object(self):
        return self.request.user


class ForgetPassword(UpdateAPIView):
    serializer_class = CreateUserSerializer
    def get_object(self):
        email=self.request.data['email']
        return User.objects.filter(email=email)
    def post(self, request):
        data = request.Post
        code = data['code']
        email = data['email']
        if check_email_code(code, email, deleted=False) == False:
            return Response({'message': 'code is wrong'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message':'verify success'},status=status.HTTP_200_OK)

class UserAuthorizeView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        data = request.data
        if data['email'] != '':
            return response
        return Response({'message': 'email is wrong'})
