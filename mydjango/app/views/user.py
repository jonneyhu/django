from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,RetrieveAPIView,ListCreateAPIView
from rest_framework_jwt.views import ObtainJSONWebToken

from app.serializers.user import CreateUserSerializer,UserDetailSerializer


class UserView(CreateAPIView):
    serializer_class = CreateUserSerializer

class UserDetail(RetrieveAPIView):
    serializer_class =UserDetailSerializer
    permissions = [IsAuthenticated]
    def get_object(self):
        return self.request.user


class UserAuthorizeView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response=super().post(request, *args, **kwargs)
        data=request.data
        if data['email']=='849248269@qq.com':
            return response
        return Response({'message':'email is wrong'})