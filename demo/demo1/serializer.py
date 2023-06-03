from .models import Employee
from .models import user
from rest_framework import serializers
from .models import *


class EmployeeSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Employee
        fields = '__all__'
    def create(self, validated_data):

        return Employee.objects.create(**validated_data)
    
    # def update(self, employee, validated_data):
    #     newemployee = employee(**validated_data)
    #     newemployee.id =employee.id
    #     newemployee.save()
    #     return newemployee 
        

class Usersr(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'