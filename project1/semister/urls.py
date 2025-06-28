from django.urls import path
from django.urls import path
from .import views
urlpatterns=[
    path('semister/',views.semister,name='semister'),
]