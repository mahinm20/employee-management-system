# Generated by Django 4.1 on 2022-09-11 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeprofile', '0009_remove_employee_task_tasks_task_assigned'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tasks',
        ),
    ]