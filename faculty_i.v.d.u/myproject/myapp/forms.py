from django.forms import fields
from.models import FacultyModel
from django import forms
class FacultyForm(forms.ModelForm):
    class Meta:
        model = FacultyModel
        fields = '__all__'        

