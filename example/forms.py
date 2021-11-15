from django import forms
from django.db import models
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name','last_name','address')
        
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'    