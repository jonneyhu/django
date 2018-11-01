from django.urls import path
from app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path(r'users', views.UserList.as_view()),
    path(r"snippets",views.Snippet_list.as_view()),
    path(r'snippet/<int:pk>',views.Snippet.as_view()),
    path(r'books',views.Books.as_view()),
    path(r'book/(?p<name>)',views.BookDetail.as_view()),
    path(r'auths',views.Auths.as_view()),
    path(r'auth/<int:name>',views.AuthDetail.as_view())

]
urlpatterns=format_suffix_patterns(urlpatterns)