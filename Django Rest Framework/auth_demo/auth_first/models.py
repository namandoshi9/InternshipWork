from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=15, null=True)
    age = models.IntegerField(null=True)
    dob = models.DateField(null=True)