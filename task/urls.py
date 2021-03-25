from django.urls import path,include
from .views import TaskView
from rest_framework import routers 




router = routers.DefaultRouter() 
router.register(r'task',TaskView)
urlpatterns =[
    path('api/',include(router.urls))


]