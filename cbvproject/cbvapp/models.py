from django.db import models

# Create your models here.

class course(models.Model):
    coursename = models.CharField(max_length=30)
    author = models.CharField(max_length=20)

