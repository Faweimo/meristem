from django import forms
from django.db import models
from .models import Client
from client.models import ClientDetail
class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientDetail
        fields = ('first_name','surname','address')
        
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'    