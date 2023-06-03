from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import*
from rest_framework import status
from django.http import Http404
from rest_framework import mixins , generics

# Create your views here.

class courselist(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = course.objects.all()
    serializer_class = courseser
    def get(self, request):
        return self.list(request)
    def post(self , request):
        return self.create(request)
    
class coursedetailview(generics.GenericAPIView , mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = course.objects.all()
    serializer_class = courseser
    def get(self , request, pk):
        return self.retrieve(request,pk)
    def put(self , request, pk):
        return self.update(request, pk)
    def delete(self , request, pk):
        return self.destroy(request, pk)

# class courselist(APIView):
#     def get(self, request):
#         courses = course.objects.all()
#         ser = courseser(courses, many=True)
#         return Response(ser.data)
    
    
#     def post(self, request):
#         coursesr = courseser(data=request.data)

#         if coursesr.is_valid():
#              coursesr.save()
#              return Response(coursesr.data , status=status.HTTP_204_NO_CONTENT)
         
#         return Response(coursesr.errors)
    
# class coursedetailview(APIView):

#     def get_course(self, pk):
#         try:
#             courses = course.objects.get(pk=pk)
#             return courses
#         except course.DoesNotExist:
#             raise Http404
            

#     def get(self, request , pk):
#         courses=self.get_course(pk)
#         ser = courseser(courses)
#         return Response(ser.data)

    

#     def delete(self , request , pk):
#        courses = self.get_course(pk)
#        courses.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)

#     def put(self , request , pk):
#       courses = self.get_course(pk)
#       coursesr = courseser(courses, data=request.data)
#       if(coursesr.is_valid()):
#            coursesr.save()
#            return Response(coursesr.data)
       
#       return Response(coursesr.errors)  