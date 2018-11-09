from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from app.models import User
from app.serializers.admin import AdminSerializer


class ListAdmin(ListCreateAPIView):
      serializer_class = AdminSerializer
      permission_classes = IsAdminUser
      def get_queryset(self):
          data=self.request.data
          query=data['query']
          return User.objects.filter(username=query,is_superuser=True)