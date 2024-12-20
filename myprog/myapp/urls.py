"""
URL configuration for myprog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.login_view,name='login'),
    path('dashboard/',views.main,name='main'),
    path('division/',views.division,name='division'),
    path('office/',views.office,name='office'),
    path('position/',views.position,name='position'),
    path('employee/',views.employee,name='employee'),
    path('nature_of_travel/',views.nature_travel,name='nature_travel'),
    path('travel_order/',views.travel,name='travel'),
    path('assign_travel/',views.assigntravel,name='assign_travel'),
    path('test/',views.test,name='test'),
    path('training_list/',views.training_list,name='training_list'),
    path('trainings/<int:employee_id>/', views.view_trainings, name='view_trainings'),
     path('logout/', views.logout_view, name='logout'),
]
