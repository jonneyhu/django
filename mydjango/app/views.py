from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from django.contrib.auth.models import User,Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status

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

class Snippet_list(APIView):
    @csrf_exempt
    def get(self,request,format=None):
            snippets=Snippet.objects.all()
            serializer=SnippetSerializer(snippets,many=True)
            data=serializer.data
            return Response(data)
    def post(self,request):
            # data=JSONParser().parse(request)
            data=request.data
            serializer=SnippetSerializer(data=data)
            if serializer.is_valid():
                 serializer.save()
                 return Response(data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class Snippet(APIView):
    @csrf_exempt
    def get_object(pk):
        try:
            snippet=Snippet.objects.filter(pk=pk)
        except Snippet.DoesNotExist:
            return HttpResponse(status=404)
    def get(self,request,pk):
            snippet=self.get_object(pk)
            serializer=SnippetSerializer(snippet)
            return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
            data=request.data
            snippet=self.get_object(pk=pk)
            serializer=SnippetSerializer(snippet,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
            snippet=self.get_object(pk)
            snippet.delete()
            return Response(status=status.HTTP_200_OK)




