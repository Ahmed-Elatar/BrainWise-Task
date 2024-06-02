from rest_framework import serializers
from .models import *






class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = "__all__"
        



class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['company','name']



class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields="__all__"
        depth=1