from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path ('employee/',views.employeelist,),
    path('user/', views.userlistview,),
    path('employee/<int:pk>', views.employeedetails,)

]
