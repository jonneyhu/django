from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from app.models import User
from app.serializers.admin import AdminSerializer


class ListAdmin(ListCreateAPIView):
    queryset = User.objects.filter(is_superuser=True)
    serializer_class = AdminSerializer