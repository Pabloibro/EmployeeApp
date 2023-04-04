from rest_framework import serializers
from EmployeeApp.models import Department, Employees


class DepartmentSerializer(serializer.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializer.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'