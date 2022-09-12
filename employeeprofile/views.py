from django.shortcuts import render, get_object_or_404
from .forms import EmployeeForm
from .models import Employee, Tasks
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.db import connection

from django.urls import reverse

def index(request):
    return render(request,'employeeprofile/index.html')


# Create your views here.
def emp_list(request):
    all_emp = Employee.objects.raw('SELECT * FROM employeeprofile_employee')
    #all_emp = Employee.objects.all()
    #print(all_emp)
    #print(connection.queries)

    return render(request,'employeeprofile/emp_list.html',{'data':all_emp})

def details(request,employee_id):
    #details =  Employee.objects.raw('SELECT * FROM employeeprofile_employee where id = %s',[employee_id])
    #details =  Employee.objects.filter(id=employee_id)
    details = get_object_or_404(Employee,pk=employee_id)
    tasks = Tasks.objects.filter(task_assigned=details)
    
    return render(request,'employeeprofile/emp_details.html',{'details':details,'tasks':tasks})
    

    



def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/emp/index/")
    form = EmployeeForm()
    return render(request,'employeeprofile/add_employee.html',{'form':form})    

def edit_details(request,employee_id):
    #details = Employee.objects.raw('SELECT * FROM employeeprofile_employee where id = %s',[employee_id])
    details =  get_object_or_404(Employee,pk=employee_id)
    form = EmployeeForm(request.POST or None,instance=details)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('details',args=(details.id,)))  
    return render(request,'employeeprofile/edit_details.html',{'form':form})    

def delete_employee(request,employee_id):
    cursor = connection.cursor()
    cursor.execute('DELETE FROM employeeprofile_employee where id=%s',[employee_id])
    return HttpResponseRedirect("/emp/index/")
