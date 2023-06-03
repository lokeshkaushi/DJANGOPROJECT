from email.policy import default
from sqlite3 import Timestamp
from tabnanny import verbose
#from random import choices
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    
    category = models.CharField(max_length=50)

    


class Blog(models.Model):
    tag_name = models.CharField(max_length=100,default='')
    blog_name = models.CharField(max_length=200,default='')
    created_date = models.DateTimeField('date created', default=timezone.now)

    update_date =models.DateTimeField(default='')
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    images= models.ImageField(upload_to='images/',null = True,blank =True)
    is_approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_date']
    @classmethod
    def updatecreated_date (Blog,blog,id,created_date):
        blog = Blog.objects.filter(blog_id = 'blog_id')
        blog=blog.first()
        blog.created_date = created_date
        blog.save()
        return blog



class Search(models.Model):

    
    food = models.CharField(max_length=50)
    Travel = models.CharField(max_length=50)
    Fashion = models.CharField(max_length=50)
    Technology = models.CharField(max_length=50)





