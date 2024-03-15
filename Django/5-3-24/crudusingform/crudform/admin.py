from django.contrib import admin
from .models import Employee
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("email","age", "salary", "name", "id")[::-1]  # Reverse the order of fields