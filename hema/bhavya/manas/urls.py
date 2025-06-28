from django.shortcuts import render
from django.urls import path
from.import views
urlpatterns=[
    path("home/",views.home,name='home'),
]


# Create your views here.
