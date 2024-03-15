# forms.py
from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['full_name', 'email', 'phone_number', 'password']
        # Add other fields as needed


        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'info fname'}),
            'email': forms.EmailInput(attrs={'class': 'info'}),
            'phone_number': forms.TextInput(attrs={'class': 'info'}),
            'password': forms.EmailInput(attrs={'class': 'info'}),
        }
