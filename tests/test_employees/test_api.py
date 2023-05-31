import random
import pytest

from django.urls import reverse
from rest_framework import status


pytestmark = pytest.mark.django_db


@pytest.fixture
def client(api_client):
    return api_client()

@pytest.fixture
def department_first(department_factory):
    return department_factory.create()

@pytest.fixture
def department_second(department_factory):
    return department_factory.create()

@pytest.fixture
def batch_employees_20(employee_factory):
    return employee_factory.create_batch(20)

@pytest.fixture
def batch_employees_first_dep(employee_factory, department_first):
    return employee_factory.create_batch(20, department=department_first)

@pytest.fixture
def batch_employees_second_dep(employee_factory, department_second):
    return employee_factory.create_batch(20, department=department_second)

@pytest.fixture
def target_employee(batch_employees_20):
    return random.choice(batch_employees_20)


class TestEmployeesEndpoints:
    url_list = 'employee-list'

    def test_list(self, client, batch_employees_20):
        response = client.get(reverse(self.url_list))

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 20
        # test pagination
        assert len(response.data['results']) == 10

    def test_list_filter_name(self, client, batch_employees_20, target_employee):
        search_name = target_employee.name.split()[0]  # last_name
        response = client.get(reverse(self.url_list), {'name': search_name})

        assert response.status_code == status.HTTP_200_OK
        # TODO exact match target with search
        assert response.data['count'] < 20

    def test_list_filter_department(
            self,
            client,
            department_first,
            batch_employees_first_dep,
            batch_employees_second_dep,

        ):
        response = client.get(reverse(self.url_list), {'department_id': department_first.id})

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 20
