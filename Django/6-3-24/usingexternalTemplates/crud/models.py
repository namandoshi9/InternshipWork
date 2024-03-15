# models.py
from django.db import models

class Registration(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    # Add other fields as needed

    def __str__(self):
        return self.full_name
