from urllib import response
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpResponse
from .models import Employee
from .models import user
from rest_framework.response import Response
from .serializer import EmployeeSerializer
from .serializer import Usersr
from django.views.decorators.csrf import  csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
#  Create your views here.

@api_view(['GET', 'POST'])
def employeelist(request):
     if request.method == 'GET':   
        employee = Employee.objects.all()
        str = EmployeeSerializer(employee , many = True)
        return Response(str.data)
     
     elif request.method == 'POST': 
        #  jsonData = JSONParser().parse(request)
         serialiser = EmployeeSerializer(data = request.data) 
         if serialiser.is_valid():
                serialiser.save()
                return Response(serialiser.data) 
         else:
              return Response(serialiser.errors)

@api_view(['GET'])
def userlistview(request):
    userlist = user.objects.all()
    usr = Usersr(userlist, many = True)
    return Response(usr.data)

@api_view(['GET','DELETE','PUT'])
# @csrf_exempt
def employeedetails(request , pk):
    try:
         employee = Employee.objects.get(pk=pk)

    except Employee.DoesNotExist:
         return Response(status =404)        
        
        
    if request.method =='DELETE':
          employee.delete()
          return Response(status = status.HTTP_204_NO_CONTENT)
     
    elif request.method == 'GET':
         seriliser = EmployeeSerializer(employee)
         return Response(seriliser.data)
         
    elif request.method == 'PUT':
        # jsonData = JSONParser().parse(request)
        employee = Employee.objects.get(pk=pk)
        serialiser = EmployeeSerializer( employee,data =request.data) 
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data) 
        else:
            return Response(serialiser.errors)
    
    # elif request.method == 'PUT':             
    #     tutorial_data = JSONParser().parse(request) 
    #     tutorial_serializer = EmployeeSerializer(employee, data=tutorial_data) 
    #     if tutorial_serializer.is_valid(): 
    #         tutorial_serializer.save() 
    #         return JsonResponse(tutorial_serializer.data) 
    #     return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

