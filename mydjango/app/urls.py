from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework.authtoken import views
from app.views.notification import NotificationResource
from app.views.user import UserView,UserAuthorizeView,UserDetail
from app.views.sms_email import Email
from app.views.withdraw import ListWithdraw,RetrieveWithdraw

urlpatterns=[
    path(r'user/',UserDetail.as_view()),
    path(r'register/',UserView.as_view()),
    path(r'login/',UserAuthorizeView.as_view()),
    path(r'email/',Email.as_view()),
    path(r'withdraw/',ListWithdraw.as_view()),
    path(r'withdraw/<int:pk>/',RetrieveWithdraw.as_view()),
    path(r'notification/',NotificationResource.as_view()),

]
urlpatternsk=format_suffix_patterns(urlpatterns)