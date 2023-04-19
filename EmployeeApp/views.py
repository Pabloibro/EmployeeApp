from django.shortcuts import render
from rest_framework import viewsets
from EmployeeApp.models import Employee, Book
from EmployeeApp.serializers import  EmployeeSerializer, BookSerializer

# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all().order_by('-id')


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        cover = request.data['cover']
        title = request.data['title']
        Book.objects.create(title=title, cover=cover)
        return HttpResponse({'message': 'Book created'}, status=200)