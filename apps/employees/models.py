from django.db import models


class Employee(models.Model):
    name = models.CharField(blank=False, db_index=True, max_length=200)
    photo = models.ImageField()
    position = models.CharField(blank=False, max_length=200)
    salary = models.DecimalField(decimal_places=2, max_digits=11)
    # TODO лучше хранить дату рождения чем возраст
    birthday = models.DateField()
    department = models.ForeignKey('Department', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Department(models.Model):
    title = models.CharField(blank=False, max_length=200)
    # TODO связь с директором лучше сделать через django_guardian, если будет время
    # director = models.OneToOneField(Employee, on_delete=models.PROTECT, related_name='managed_department')

    def __str__(self):
        return self.title
