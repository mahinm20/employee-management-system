from django.shortcuts import render
from api.serializers import EmployeeSerializer
from employeeprofile.models import Employee
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView,DestroyAPIView


class ListEmployeeView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CreateEmployeeView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UpdateEmployeeView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeleteEmployeeView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

