from django import forms
from .models import *

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user', 'neighbourhood_id']


