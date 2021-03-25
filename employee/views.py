from django.shortcuts import render
from .models import employee
from rest_framework import viewsets
from .serializers import employee_serializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class employeView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = employee.objects.all()
    serializer_class = employee_serializer