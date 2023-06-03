from django.contrib import admin
from django.urls import path
from .views import courselist , coursedetailview
from .import views


urlpatterns = [

    path('courses/', courselist.as_view()),
    path('courses/<int:pk>/', coursedetailview.as_view()),
    
]