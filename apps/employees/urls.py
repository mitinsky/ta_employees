from django.urls import path, include
from rest_framework import routers

from .views import EmployeeModelViewSet


router = routers.DefaultRouter()
router.register('', EmployeeModelViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
]
