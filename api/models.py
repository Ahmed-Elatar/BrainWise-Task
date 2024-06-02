from django.db import models
from django.contrib.auth.models import AbstractUser

# class User():
#     ROLE_CHOICES = (
#         ('Admin', 'Admin'),
#         ('Manager', 'Manager'),
#         ('Employee', 'Employee'),
#     )
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Employee')

class Company(models.Model):
    name = models.CharField(max_length=255)
    number_of_departments = models.PositiveIntegerField(default=0)
    number_of_employees = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Department(models.Model):
    company = models.ForeignKey(Company, related_name='departments' , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    number_of_employees = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    



class Employee(models.Model):
    
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    designation = models.CharField(max_length=255)
    hired_on = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
