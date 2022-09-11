from django.urls import path
from . import views

urlpatterns = [
    path("add/",views.add_employee,name="add"),
    path("index/",views.index,name="index"),
    path("list/",views.emp_list,name="list"),
    path("details/<int:employee_id>/",views.details,name='details'),
    path("edit/<int:employee_id>/",views.edit_details,name="edit"),
    path("remove/<int:employee_id>/",views.delete_employee,name="remove"),
]
