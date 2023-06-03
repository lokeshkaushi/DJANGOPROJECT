from .models import *
from rest_framework import serializers


class courseser(serializers.ModelSerializer):
    class Meta:
        model = course
        fields ='__all__'