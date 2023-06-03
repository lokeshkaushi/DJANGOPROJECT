from django.db import models

# Create your models here.
# Create your models here.
class Employee(models.Model):
    name  = models.CharField(max_length=30)
    email = models.EmailField(max_length=30 ) 
    password = models.CharField(max_length=10)
    phone = models.IntegerField()  

class user(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    
    