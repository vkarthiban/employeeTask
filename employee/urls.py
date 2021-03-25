from django.urls import path,include
from .views import employeView
from rest_framework import routers 




router = routers.DefaultRouter() 
router.register(r'employee',employeView)
urlpatterns =[
    # path('employee',employeView.as_view({'get':'list'})),
    # path('emplyee')
    path('api/',include(router.urls))


]