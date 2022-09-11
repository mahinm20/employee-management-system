from django.urls import path
from .views import ListEmployeeView, CreateEmployeeView, UpdateEmployeeView,DeleteEmployeeView

app_name = "api"

urlpatterns = [
    path("",ListEmployeeView.as_view(),name="list"),
    path("create/",CreateEmployeeView.as_view(),name="create"),
    path("update/<int:pk>/",UpdateEmployeeView.as_view(),name="update"),
    path("delete/<int:pk>/",DeleteEmployeeView.as_view(),name="delete")
]
