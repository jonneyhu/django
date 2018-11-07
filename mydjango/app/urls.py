from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework.authtoken import views
from app.views.user import UserView
urlpatterns=[
    # path(r'token/',views.obtain_auth_token),
    path(r'register/',UserView.as_view()),
]
urlpatternsk=format_suffix_patterns(urlpatterns)