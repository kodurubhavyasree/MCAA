from django.urls import path
from .import views
urlpatterns=[
     path('delete_employee/,<int:pk>)',views.delete_employee,name='delete_employee'),
]
