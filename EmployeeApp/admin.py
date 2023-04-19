from django.contrib import admin
from .models import Employee, Book

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'contact', 'address']
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Book)