from django import forms 
from .models import ClientDetail

class ClientDetailForm(forms.ModelForm):
    
    class Meta:
        model           = ClientDetail
        # fields          = ('title','first_name','surname','other_name','phone_number','address','company_name','company_address','means_of_identification','identification_number','PFA','RSA','address','will_executors','options')
        fields = '__all__'
        widgets         = {
            'title':forms.TextInput(attrs={
            'type':'text',
            'id':'person_title',
            'placeholder':'e.g Mr.'
        }),
        'surname':forms.TextInput(attrs={
            'type':'text',
            'id':'person_surname',
            
           
        }),
        'first_name':forms.TextInput(attrs={
            'type':'text',
            'id':'person_firstname',
           
        }),
        'other_name':forms.TextInput(attrs={
            'type':'text',
            'id':'person_othername',
           
        }),
        'phone_number':forms.TextInput(attrs={
            'type':'text',
            'id':'person_phone',
           
        }),
        'address':forms.TextInput(attrs={
            'type':'text',
            'id':'person_address',
           
        }),
        'company_name':forms.TextInput(attrs={
            'type':'text',
            'id':'person_company',
           
        }),
        'company_address':forms.TextInput(attrs={
            'type':'text',
            'id':'person_companyAddress',
           
        }),
        'means_of_identification':forms.Select(attrs={
            'type':'text',
            'id':'means_of_id',
            'class':'frm-field required sect',
            'style':'height:40px;border-radius:0px',
            'selected':'true'
            
           
        }),
        'will_executors':forms.Select(attrs={
            'type':'text',
            'id':'country',
            'class':'frm-field required sect',
            'style':'height:40px;border-radius:0px',
            'label':"Placeholder"
            
           
        }),
        'identification_number':forms.TextInput(attrs={
            'type':'text',
            'id':'person_idNumber',
           
        }),
        'PFA':forms.TextInput(attrs={
            'type':'text',
            'id':'person_pfa',
           
        }),'RSA':forms.TextInput(attrs={
            'type':'text',
            'id':'person_rsaNumber',
           
        }),
        'options':forms.TextInput(attrs={
            'type':'text',
            'id':'will_executors_others',
           
        }),
        'bank_name':forms.Select(attrs={
            'type':'text',
            'id':'bank_name',
            'class':'person_bankName frm-field required sect',
            'style':'height:40px;border-radius:0px'
           
        }),
        'account_number':forms.TextInput(attrs={
            'type':'text',
            'id':'person_accountNumber',
            'class':'person_moreAccountNumber'
           
        }),
        'branch':forms.TextInput(attrs={
            'type':'text',
            'id':'person_accountBranch',
            'class':"person_moreBranch" 
           
        }),
        'full_name':forms.TextInput(attrs={
            'type':'text',
            'id':'beneficiary_fullname',
            'style':'padding-left:5px;'
           
        }),
        'address_beneficiary':forms.TextInput(attrs={
            'type':'text',
            'id':'beneficiary_address',
            'style':'padding-left:5px;'
           
        }),
        'phone_number_beneficiary':forms.TextInput(attrs={
            'type':'text',
            'id':'beneficiary_phone',
            'style':'padding-left:5px;'
           
        }),
         'bank_name_beneficiary':forms.TextInput(attrs={
            'type':'text',
            'id':'person_title',
            'style':'padding-left:5px;'
           
        }),
         'email':forms.EmailInput(attrs={
            'type':'text',
            'id':'beneficiary_email',
            'style':'padding-left:5px;'
           
        }),
         'values':forms.TextInput(attrs={
            'type':'text',
            'id':'beneficiary_shareValues',
            'style':'padding-left:5px;'
           
        }),
        }
  