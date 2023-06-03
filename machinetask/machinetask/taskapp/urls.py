from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('order/', OrderViewSet.as_view()),
    path('order_edit/<int:pk>/', order_edit.as_view()),
    
    
     

 ]