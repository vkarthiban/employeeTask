from django.db import models

# Create your models here

class employee(models.Model):
    Name        = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    DateOfJoin  = models.DateField()