from rest_framework import serializers
from employeeprofile.models import Department, Employee,Salary, Role

class EmployeeSerializer(serializers.ModelSerializer):
    #salary_per_annum = serializers.CharField(source='salary.salary_package')
    #department = serializers.CharField(source='department.get_department_name')
    #role_assigned = serializers.CharField(source='roles.role_name')
    #manager_name = serializers.CharField(source='manager')

    
    class Meta:
        model = Employee
        #fields = ('id','first_name','last_name','email','phone_number','address','salary_per_annum','department','role_assigned','manager_name')
        fields = '__all__'