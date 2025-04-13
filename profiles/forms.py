from django import forms
from .models import *

class infoform(forms.ModelForm):
    fname = forms.CharField(label='First Name')
    lname = forms.CharField(label='Last Name',required=False)
    tech = forms.CharField(label='Technology')
    email = forms.EmailField(label='Email Id')
    photo = forms.FileField()

    class Meta:
        model = info
        exclude = ['date']

from django.forms.widgets import NumberInput
class searchform(forms.Form):
    select = forms.DateField(widget=NumberInput(attrs={'type':'date'}),label='date')

