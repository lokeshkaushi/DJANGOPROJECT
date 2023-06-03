from ast import Try, parse
from datetime import datetime, timedelta
from http.client import HTTPResponse
from re import search
from django.shortcuts import HttpResponse
from multiprocessing import context
from turtle import title
from typing_extensions import Self
from unicodedata import category
from unittest import load_tests
from urllib import request
from venv import create
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework import generics 
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from .models import Category
from rest_framework.generics import ListAPIView 
from rest_framework.response import Response
from rest_framework import generics ,response
from rest_framework import status
from .serializers import *
from rest_framework.decorators import api_view,parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import urllib.request



class CategoryListView(generics.ListAPIView):
    queryset = Blog.objects.all()
  
    serializer_class =BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['blog_name']
    Search_fields = ['Category']
   
class BlogViewSet(APIView):
  def get(self, request):
    social = Blog.objects.all()
    serializer = BlogSerializer(social , many = True)
    return Response(serializer.data) 
  def post(self , request) :
    serializer = BlogSerializer(data=request.data) 
    if serializer.is_valid():              
      serializer.save()  
      return Response("Blog create successfully done")  
    else:
      return Response(serializer.errors)  
  
@api_view(['GET','POST','PUT','PATCH'])
#@permission_classes((IsAuthenticated, ))
@parser_classes([FormParser,MultiPartParser])
def blog_update(request,pk):
    if request.method == 'GET':
      blog = Blog.objects.get(id=pk)
      serializer = BlogSerializer(blog, many = False)
      return Response(serializer.data)
    elif request.method == 'POST':
      blog = Blog.objects.get(id=pk)
      serializer = BlogSerializer(instance=blog, data=request.data )
      if serializer.is_valid():
          serializer.save()
    elif request.method == 'PUT':
      blog = Blog.objects.get(id=pk)
      serializer = BlogSerializer(instance=blog, data =request.data)
      if serializer.is_valid():
          serializer.save()
      return Response(serializer.data)
    elif request.method == 'PATCH':
      blog = Blog.objects.get(id=pk)
      serializer = BlogSerializer(instance=blog,data=request.data )
      if serializer.is_valid():
          serializer.save()
      return Response(serializer.data)
@api_view(['DELETE'])
def blog_delete(request,pk):
        blog = Blog.objects.get(id=pk)
        blog.delete()
        return Response("Blog is successfully delete")  

@csrf_exempt
def Like_Blog(request,id):
    post = Blog.objects.filter(id = id)
    if request.user in post[0].likes.all():
       Blog[0].likes.remove(request.user)
    else:
        Blog[0].likes.add(request.user)
    return response.Response(status=status.HTTP_202_ACCEPTED) 


class SearchListView(generics.ListAPIView):
    
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filterset_fields = ['tag_name']
    Search_fields = ['created_date']
    def latest(request):
        blog=Blog.objects.order_by('-created_date')
        serializer = BlogSerializer(blog , many = True)
        return Response(serializer.data)
    def oldest(request):
        blog=Blog.objects.order_by('created_date')
        serializer = BlogSerializer(blog , many = True)
        return Response(serializer.data)



@api_view(('GET',))
@parser_classes([FormParser,MultiPartParser])
def latest(request):
    blog=Blog.objects.order_by('-created_date')
    serializer = BlogSerializer(blog , many = True)
    return Response(serializer.data)
    

@api_view(('GET',))
@parser_classes([FormParser,MultiPartParser])
def oldest(request):
    blog=Blog.objects.order_by('created_date')
    serializer = BlogSerializer(blog , many = True)
    return Response(serializer.data)
      
@api_view(('GET',))
@parser_classes([FormParser,MultiPartParser])

def popular(self,Blog, created_date, order='ASC', tzinfo=None):
    search = request.GET.get('search','')
    category= request.GET.get('category','')

    if search:
        blog= Blog.objects.filter(Q(blog_name_icontains=search)|Q(brand_icontains=search))
    else:
        blog = Blog.objects.all()

    if category:
        category = Category.filter(category_it= category)

        return Response(serializer.data)  
        
        '''assert Blog in ('year', 'month', 'week', 'day', 'hour', 'minute', 'second'), \
            "'kind' must be one of 'year', 'month', 'week', 'day', 'hour', 'minute', or 'second'."
        assert order in ('ASC', 'DESC'), \
            "'order' must be either 'ASC' or 'DESC'."
        if settings.USE_TZ:
            if tzinfo is None:
                tzinfo = timezone.get_current_timezone()
        else:
            tzinfo = None
        return self.annotate(
            created_date=Blog(created_date,Blog, output_field=created_date(), tzinfo=tzinfo),
            plain_field=F(created_date)
        ).values_list(
            'datetimefield', flat=True
        ).distinct().filter(plain_field__isnull=False).order_by(('-' if order == 'DESC' else '') + 'created_date')
   #blogs = Blog.objects.filter(created_date='created_date')'''
'''context = {'PostList': blogs()}
   serializer = BlogSerializer(blogs , many = True)
    # the error was here
   return render_to_response(serializer, context)'''
'''blog=Blog.objects.order_by(created_date='2022-10-19 00:00+0000')
   serializer = BlogSerializer(blog , many = True)
   return Response(serializer.data)
   #response = self.user.get("/api/v1/events/?timestamp=2022-10-19 00:00+0000", **{'HTTP_ACCEPT': 'application/json'})'''  

''' params= kwargs
      params_list = params['id'].split('-')
      blog=Blog.objects.filter(params_list[2])
    
      serializer = BlogSerializer(blog , many = True)
      return Response(serializer.data)'''
      
     
    

