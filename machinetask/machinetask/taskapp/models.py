from django.db import models


class Order(models.Model):
    order_id = models.AutoField(auto_created=True,primary_key=True)
    order_name = models.CharField(max_length=100)
    order_price = models.FloatField()
    order_quantity = models.PositiveIntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
    mobile_no = models.IntegerField()
    deliver_to = models.CharField(max_length=100)


# Create your models here.
