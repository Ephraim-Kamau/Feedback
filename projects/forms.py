from django import forms
from .models import Profile,Topics

class NewProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude = []

class NewTopicsForm(forms.ModelForm):
    class Meta:
        model=Topics
        exclude = []        