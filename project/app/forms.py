from django import forms
from .models import*


class Emplayeeform(forms.ModelForm):
    class Meta:
        model=EmplayeeModel
        fields='__all__'