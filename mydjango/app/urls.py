from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework.authtoken import views
from app.views.user import UserView,UserAuthorizeView,UserDetail
urlpatterns=[
    path(r'user/',UserDetail.as_view()),
    path(r'register/',UserView.as_view()),
    path(r'login/',UserAuthorizeView.as_view())
]
urlpatternsk=format_suffix_patterns(urlpatterns)