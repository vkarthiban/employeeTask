from django.db import models
from employee.models import employee
# Create your models here.
class Task(models.Model):
    name       = models.CharField( max_length=100)
    start_date = models.DateTimeField()
    end_date   = models.DateTimeField()
    complete_time = models.TimeField()
    assigned_to = models.ForeignKey(employee ,related_name='tasks', on_delete=models.CASCADE)