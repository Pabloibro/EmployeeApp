from django.shortcuts import render
from rest_framework import viewsets
from EmployeeApp.models import Employee
from EmployeeApp.serializers import  EmployeeSerializer

# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all().order_by('-id')