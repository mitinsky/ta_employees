import pytest
from pytest_factoryboy import register

from rest_framework.test import APIClient

from test_employees.factories import DepartmentFactory, EmployeeFactory, UserFactory


register(DepartmentFactory)
register(EmployeeFactory)


@pytest.fixture
def api_client():

    def return_user_api_client(user=None):
        client = APIClient()

        if not user:
            user = UserFactory()
        client.login(username=user.username, password='password')

        return client

    return return_user_api_client

@pytest.fixture
def api_anon_client():
    return APIClient
