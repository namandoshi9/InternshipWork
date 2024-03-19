from django.urls import path
from .views import *

urlpatterns = [
    path('employeeapi/', EmployeeViewset.as_view()),
    path('employeeapi/<int:id>', EmployeeViewset.as_view()),

]