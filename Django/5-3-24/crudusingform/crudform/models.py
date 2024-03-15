from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    salary = models.IntegerField()
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} - {self.age}"