from django.urls import path, include
from rest_framework import routers

from .views import EmployeeModelViewSet, DepartmentModelViewSet


router = routers.DefaultRouter()
router.register('employees', EmployeeModelViewSet, basename='employee')
router.register('departments', DepartmentModelViewSet, basename='department')

urlpatterns = [
    path('', include(router.urls)),
]
