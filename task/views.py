from django.shortcuts import render
from .models import Task
from rest_framework import viewsets
from .serializers import Task_serializer
# Create your views here.


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = Task_serializer