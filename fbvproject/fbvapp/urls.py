from django.contrib import admin
from django.urls import path
from .views import courselistview, coursedetailview
from . import views
urlpatterns = [
    path('courses/', views.courselistview , name='courselistview'),
    path('courses/<int:id>/',views.coursedetailview , name='coursedetailview'),
]
      