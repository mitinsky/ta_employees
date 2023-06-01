import django_filters
from rest_framework import viewsets, status, serializers

from .models import Employee, Department


# TODO move to serializers.py
class EmployeeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class DepartmentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Employee
        fields = ['name', 'department_id', ]


class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    filterset_class = EmployeeFilter


class DepartmentModelViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer
    pagination_class = None
