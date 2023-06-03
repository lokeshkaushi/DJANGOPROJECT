from .models import*
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import generics


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['category']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__" 
 


class SearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Search
        fields = ['tag_name','blog_name','created_date','update_date','images','is_approved',]

