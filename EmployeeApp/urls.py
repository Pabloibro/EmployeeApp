from django.urls import path, include
from rest_framework import routers
from .views import EmployeeViewSet,BookViewSet


router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'book', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]