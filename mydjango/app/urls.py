from django.urls import path
from app import view
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
urlpatterns=[
    path(r'token/',views.obtain_auth_token),
    path(r'register/',view.User.as_view())
]
urlpatterns=format_suffix_patterns(urlpatterns)