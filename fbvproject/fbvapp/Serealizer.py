from rest_framework import serializers
from .models import *


class courseSer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'