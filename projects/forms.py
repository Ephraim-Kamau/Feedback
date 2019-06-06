from django import forms
from .models import Profile,Topics,Comments

class NewProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude = []

class NewTopicsForm(forms.ModelForm):
    class Meta:
        model=Topics
        exclude = []        

class NewCommentsForm(forms.ModelForm):
    class Meta:
        model=Comments
        exclude = []          