import pytest

from django.urls import reverse

from apps.employees.models import Employee, Department


pytestmark = pytest.mark.django_db


@pytest.fixture
def department(department_factory):
    return department_factory.create()


class TestEmployeesEndpoints:
    url_list = 'employees-list'

    def test_list(self, department):
        assert True
