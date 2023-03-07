from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dipartment=models.CharField(max_length=50)
    experience=models.IntegerField(max_length=50)
    email=models.EmailField()
    
