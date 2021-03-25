from django.shortcuts import render
from .models import employee
from rest_framework import viewsets
from .serializers import employee_serializer
# Create your views here.


class employeView(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = employee_serializer