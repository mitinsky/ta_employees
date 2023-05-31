import factory
from faker import Faker

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile

from apps.employees import models


faker = Faker('ru_Ru')


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.LazyAttribute(lambda x: faker.user_name())
    email = factory.LazyAttribute(lambda x: faker.email())
    plaintext_password = factory.PostGenerationMethodCall('set_password', 'password')

    class Meta:
        model = get_user_model()
        exclude = ['plaintext_password']


class DepartmentFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.company())

    class Meta:
        model = models.Department


class EmployeeFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: faker.name())
    photo = factory.LazyAttribute(
        lambda x: ContentFile(
            factory.django.ImageField()._make_data(
                {'width': 1024, 'height': 768}
            ), 'user_photo.jpg'
        )
    )
    position = factory.LazyAttribute(lambda x: faker.job())
    salary = factory.LazyAttribute(lambda x: faker.random_int(min=1000, max=1000000))
    birthday = factory.LazyAttribute(lambda x: faker.date_of_birth(minimum_age=16))
    department = factory.SubFactory(DepartmentFactory)

    class Meta:
        model = models.Employee
