from django import forms
from .models import *

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user', 'neighbourhood_id']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile', 'hood']


class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['admin']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['neighbourhood_id']