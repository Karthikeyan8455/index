from django.db import models

# Create your models here.


class Employee(models.Model):
    fieldname=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    
    class Meta:
        db_table="application_employee"
