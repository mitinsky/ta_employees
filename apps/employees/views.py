import django_filters
from rest_framework import viewsets, status, serializers
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.db.models import Count, Sum

from .models import Employee, Department


# TODO move to serializers.py
class EmployeeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class DepartmentModelSerializer(serializers.ModelSerializer):
    employees_count = serializers.IntegerField()
    salary_sum = serializers.FloatField()

    class Meta:
        model = Department
        fields = ('id', 'title', 'employees_count', 'salary_sum', )


class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Employee
        fields = ('name', 'department_id', )


class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    filterset_class = EmployeeFilter
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthenticated, ]


class DepartmentModelViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentModelSerializer
    pagination_class = None
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return Department.objects.annotate(
            employees_count=Count('employees')
        ).annotate(
            salary_sum=Sum('employees__salary')
        )
