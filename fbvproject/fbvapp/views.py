from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import  Course
from .Serealizer import courseSer

# Create your views here
@api_view(['GET' , 'POST'])
def courselistview(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        coursesr = courseSer(courses, many=True)
        return Response(coursesr.data)
    
    elif request.method == 'POST':
        
         
         coursesr = courseSer(data=request.data)
         if coursesr.is_valid():
             coursesr.save()
             return Response(coursesr.data)
         
         return Response(coursesr.errors)

@api_view(['GET', 'PUT' , 'DELETE'])
def coursedetailview(request,id):

    try :
        course = Course.objects.get(id=id)
        
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        

    if request.method == 'GET':
        course = Course.objects.get(id=id)
        serializer = courseSer(course,many=False)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
       coursesr = courseSer(course, data=request.data)
       if(coursesr.is_valid()):
           coursesr.save()
           return Response(coursesr.data)
       
       return Response(coursesr.errors)

    elif request.method == 'DELETE':

        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)