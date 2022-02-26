from dataclasses import field
from pyexpat import model
from statistics import mode
from rest_framework import serializers
from EmployeeApp.models import Departments, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields  = ('DepartmentId',
                    'DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
     class Meta:
         model = Employees
         feilds = ('EmployeeId',
                    'EmployeeName',
                    'Department',
                    'DateOfJoining',
                    'photoFileName')

