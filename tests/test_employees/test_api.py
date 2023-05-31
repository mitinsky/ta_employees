import pytest

from django.urls import reverse
from rest_framework import status

from apps.employees.models import Employee, Department


pytestmark = pytest.mark.django_db


@pytest.fixture
def client(api_client):
    return api_client()

@pytest.fixture
def department(department_factory):
    return department_factory.create()

@pytest.fixture
def batch_employees_20(employee_factory):
    return employee_factory.create_batch(20)


class TestEmployeesEndpoints:
    url_list = 'employee-list'

    def test_list(self, client, batch_employees_20):
        response = client.get(reverse(self.url_list))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 20
