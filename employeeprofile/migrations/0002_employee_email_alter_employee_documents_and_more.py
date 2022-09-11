# Generated by Django 4.1 on 2022-09-09 11:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employeeprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='documents',
            field=models.FileField(blank=True, null=True, upload_to='media', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_name',
            field=models.CharField(choices=[['Intern', 'Intern'], ['Software Engineer', 'Software Engineer'], ['Manager', 'Management'], ['HR', 'HR'], ['CEO', 'CEO']], max_length=100),
        ),
    ]
