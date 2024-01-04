from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('approve_registration',views.approve_registration,name='approve_registration'),
    path('signin',views.userlogin,name='userlogin'),
    path('allrecords',views.adminPage,name='adminpage'),
    path('new_employee',views.Newemployee,name='new_employee')
]