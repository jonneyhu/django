from django.urls import path
from app import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns=[
    path(r"snippets",views.Snippet_list.as_view()),
    path(r'snippet/<int:pk>',views.Snippet.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)