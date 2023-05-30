import pytest
from pytest_factoryboy import register

from test_employees.factories import DepartmentFactory, EmployeeFactory


register(DepartmentFactory)
register(EmployeeFactory)
