from distutils.command.upload import upload
import email
from operator import mod
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.

DEPARTMENT_CHOICE = (
    ('HR','HUMAN RESOURCE'),
    ('ENGG','ENGINEERING'),
    ('ACC','ACCOUNTS'),
    ('MAN','MANAGEMENT')
)

ROLE_CHOICE = (
    ['Intern','Intern'],
    ['Software Engineer','Software Engineer'],
    ['Manager','Management'],
    ['HR','HR'],
    ['CEO','CEO']
)

class Department(models.Model):
    department_name = models.CharField(max_length=100,choices=DEPARTMENT_CHOICE)

    def __str__(self):
        return self.get_department_name_display()
    def get_department_name(self):
        return self.get_department_name_display()


class Role(models.Model):
    role_name = models.CharField(max_length=100,choices=ROLE_CHOICE)

    def __str__(self):
        return self.role_name



class Salary(models.Model):
    salary_package = models.IntegerField()
    
    def __str__(self):
        return str(self.salary_package)+" LPA"

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True,default='')
    address = models.TextField(max_length=200)
    phone_number = models.IntegerField(blank=True,null=True)
    documents = models.FileField(upload_to='media',validators=[FileExtensionValidator(['pdf'])],blank=True,null=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    roles = models.ForeignKey(Role,on_delete=models.CASCADE)
    salary = models.ForeignKey(Salary,on_delete=models.CASCADE,default="",related_name="salaries")
    manager = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)
    #task = models.ForeignKey(Tasks,null=True,blank=True,on_delete=models.CASCADE,related_name="tasks")

    def __str__(self):
        return self.first_name + " "+self.last_name
   
# class Tasks(models.Model):
#     task_assigned = models.ForeignKey(Employee,on_delete=models.CASCADE,default="")
#     task_name = models.CharField(max_length=100)
#     task_desp = models.TextField(max_length=400)
#     is_done = models.BooleanField(default=False)

#     def __str__(self):
#         return self.task_name



    
    


