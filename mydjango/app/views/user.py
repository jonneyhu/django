from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,RetrieveAPIView

from app.serializers.user import CreateUserSerializer


class UserView(CreateAPIView):
    serializer_class = CreateUserSerializer

class UserDetail():
    pass