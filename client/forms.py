from django import forms 
from .models import ClientDetail,BankDetail,BeneficiaryDetail

class ClientDetailForm(forms.ModelForm):
    class Meta:
        model           = ClientDetail
        fields          = ('title','first_name','surname','other_name','phone_number','address','company_name','company_address','means_of_identification','identification_number','PFA','RSA','address','will_executors','options')
        # widgets         = {
        #     'bank_details':forms.TextInput(attrs={
        #     'type':'hidden',
        #     'class':'form-control'
        # }
        
        # )
        # }
        
class BankDetailForm(forms.ModelForm):
    class Meta:
        model           = BankDetail
        fields          = ('bank_name','account_number','branch')
        
               
class BeneficiaryDetailForm(forms.ModelForm):
    class Meta:
        model           = BeneficiaryDetail
        fields          = ('full_name','address_beneficiary','phone_number_beneficiary','bank_name_beneficiary')
                  