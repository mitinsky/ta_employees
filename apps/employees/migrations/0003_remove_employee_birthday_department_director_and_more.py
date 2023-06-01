# Generated by Django 4.2 on 2023-06-01 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employee_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='birthday',
        ),
        migrations.AddField(
            model_name='department',
            name='director',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='managed_department', to='employees.employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
    ]