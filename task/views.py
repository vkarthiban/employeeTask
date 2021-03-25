from django.shortcuts import render
from .models import Task
from rest_framework import viewsets
from .serializers import Task_serializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class TaskView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = Task_serializer