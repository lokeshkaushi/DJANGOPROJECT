from django.urls import path,include
from .import views
from .views import*

urlpatterns = [

    path('Category/',CategoryListView.as_view()),
    path('Search/',SearchListView.as_view()),
    path('blog/', BlogViewSet.as_view()),
    
    path('Search/', views.Search, name='Search'),
    
    path('latest/', views.latest, name='latest'),
    path('oldest/', views.oldest, name='oldest'),
    path('popular',views.popular, name='popular'),
]
