from django.contrib import admin

from client.models import  ClientDetail, BankName

# Register your models here.
from .models import *
class ClientDetailAdmin(admin.ModelAdmin):
    fieldsets = (
            ('Client Details', {'fields': ('title','first_name','surname','other_name','phone_number','address','company_name','company_address','means_of_identification','identification_number','PFA','RSA','will_executors','options')}),

            ('Bank Details', {'fields': ('bank_name','account_number','branch')}),
            
            ('More Bank Details', {'fields': ('bank_name_2','account_number_2','branch_2')}),

            ('Beneficiary Details', { 'fields': ('full_name','address_beneficiary','phone_number_beneficiary','bank_name_beneficiary','email','values'),
            }),
            
            ('More Beneficiary Details', { 'fields': ('full_name_2','address_beneficiary_2','phone_number_beneficiary_2','bank_name_beneficiary_2','email_2','values_2'),
            }),
            
            

    )
admin.site.register(ClientDetail,ClientDetailAdmin)
admin.site.register(BankName)

