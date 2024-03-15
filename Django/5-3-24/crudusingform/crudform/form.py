from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Salary'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
        }

        error_messages = {
            'name': {'required': 'name is reqired'},
            'salary': {'required': 'salary is reqired!'},
        }