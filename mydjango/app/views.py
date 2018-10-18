from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User,Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from app.models import Snippet
from app.serializers import UserSerializer, GroupSerializer, SnippetSerializer


class UserViewSet(viewsets.ModelViewSet):
      queryset = User.objects.all().order_by('-date_joined')
      serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
      queryset = Group.objects.all()
      serializer_class = GroupSerializer

class JSONResponse(HttpResponse):
      def __init__(self ,data,**kwargs):
          from rest_framework.renderers import JSONRenderer
          content=JSONRenderer().render(data)
          kwargs['content_type']='application/json'
          super(JSONResponse,self).__init__(content,**kwargs)
@csrf_exempt
def snippet_list(request):
    if request.method=="GET":
        snippets=Snippet.objects.all()
        serializer=SnippetSerializer(snippets,many=True)
        data=serializer.data
        return JSONResponse(data)
    elif request.method=="POST":
        data=JSONParser().parse(request)
        serializer=SnippetSerializer(data=data)
        if serializer.is_valid():
             serializer.save()
             return JSONResponse(data,status=200)
        return JSONResponse(serializer.errors,status=400)

@csrf_exempt
def snippet_detail(pk,request):
    try:
        snippet=Snippet.objects.filter(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    if request.method=="GET":
        pass
    if request.method=="PUT":
        pass
    if request.method=="DELETE":
        pass




