from django.db import models


class Department(models.Manager):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)

class Role(models.Model):
    name = models.CharField(max_length=100,null=False)

from django.db import models

class Department(models.Model):  # Changed from models.Manager to models.Model
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)  # Changed TextField to CharField for consistency
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)  # Fixed: Use ForeignKey for relationships
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.BigIntegerField(default=0)  # Changed to BigIntegerField to store longer numbers
    hire_date = models.DateField()  # Fixed typo: 'hire_data' -> 'hire_date'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
