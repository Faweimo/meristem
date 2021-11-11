from django.contrib import admin

from client.models import BankDetail, BeneficiaryDetail, ClientDetail

# Register your models here.
from .models import *
admin.site.register(BeneficiaryDetail)
admin.site.register(BankDetail)
admin.site.register(ClientDetail)

