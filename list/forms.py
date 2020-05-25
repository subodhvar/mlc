from django.forms import ModelForm
from .models import *
from django import forms
class AligarhForm(ModelForm):
    class Meta:
        model = Aligarh_c
        fields = ['relation_name_english','address_english','name_new','MOBILE','name_english','Booth','section']
        widgets = {'Booth': forms.HiddenInput(), 'section':forms.HiddenInput(),'name_english':forms.HiddenInput()}
