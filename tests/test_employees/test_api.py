import random
import pytest
from io import BytesIO
from PIL import Image

from django.urls import reverse
from django.core.files.base import File
from rest_framework import status

from apps.employees.models import Employee


pytestmark = pytest.mark.django_db


@pytest.fixture
def client(api_client):
    return api_client()

@pytest.fixture
def userpic():
    # TODO use tmpdir
    file_obj = BytesIO()
    image = Image.new('RGBA', size=(50, 50), color=(255, 0, 0))
    image.save(file_obj, 'png')
    file_obj.seek(0)

    return File(file_obj, name='userpic.png')

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

@pytest.fixture
def new_employee_data(department_first, userpic):
    return {
        'name': 'Test test test',
        'photo': userpic,
        'position': 'position',
        'salary': 99999.99,
        'birthday': '1990-01-01',
        'department': department_first.id,
    }


class TestEmployeesEndpoints:
    url_list = 'employee-list'
    url_detail = 'employee-detail'

    def test_list(self, client, batch_employees_20):
        response = client.get(reverse(self.url_list))

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 20
        # test pagination
        assert len(response.data['results']) == 10

    # TODO parametrize
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

    def test_create_employee(self, client, new_employee_data):
        response = client.post(reverse(self.url_list), data=new_employee_data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == new_employee_data['name']

    def test_destroy_employee(self, client, batch_employees_20, target_employee):
        expected_employees_count = len(batch_employees_20) - 1
        response = client.delete(reverse(self.url_detail, args=[target_employee.id]))

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Employee.objects.count() == expected_employees_count
