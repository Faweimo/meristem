from django.shortcuts import redirect, render
from django.http import HttpResponse

from client.models import BeneficiaryDetail, BankDetail,ClientDetail
# Create your views here.
from .forms import ClientDetailForm,BeneficiaryDetailForm,BankDetailForm
        
from django.http import HttpResponseRedirect

from formtools.preview import FormPreview



def index(request):
    if request.method == 'POST':
      
        # Client Details
        title                   = request.POST['title']
        first_name              = request.POST['first_name']
        surname                 = request.POST['surname']
        other_name              = request.POST['other_name']
        phone_number            = request.POST['phone_number']
        address                 = request.POST['address']
        company_name            = request.POST['company_name']
        company_address         = request.POST['company_address']
        means_of_identification = request.POST['means_of_identification']
        identification_number   = request.POST['identification_number']
        PFA                     = request.POST['PFA']
        RSA                     = request.POST['RSA']
        address                 = request.POST['address']
        will_executors          = request.POST['will_executors']
        options                 = request.POST['options']
        bank_details            = request.POST.get('bank_details')
        beneficiary_details     = request.POST.get('beneficiary_details')
        
        
        bank_name               = request.POST['bank_name']
        account_number          = request.POST['account_number']
        branch                  = request.POST['branch']
        
        full_name               = request.POST['full_name']
        address_beneficiary     = request.POST['address_beneficiary']
        phone_number_beneficiary            = request.POST['phone_number_beneficiary']
        bank_name_beneficiary               = request.POST['bank_name_beneficiary']
        
        # try:
            # saving to client models 
        client                  = ClientDetail.objects.create()      
        bank_obj                = BankDetail(id=bank_details)
        beneficiary_obj         = BeneficiaryDetail(id=beneficiary_details)
        
        client.title            = title
        client.first_name       = first_name
        client.surname          = surname
        client.other_name       = other_name
        client.phone_number     = phone_number
        client.address          = address
        client.company_name     = company_name
        client.company_address  = company_address
        client.means_of_identification  = means_of_identification
        client.identification_number    = identification_number
        client.PFA                      = PFA
        client.RSA                      = RSA
        client.address                  = address
        client.will_executors           = will_executors
        client.options                  = options
        client.bankdetail                  = bank_obj
        client.bankdetail.bank_name                 = bank_name
        client.bankdetail.account_number                 = account_number
        client.bankdetail.branch                 = branch
        
        client.beneficiarydetail                  = beneficiary_obj
        client.beneficiarydetail.full_name               = full_name
        client.beneficiarydetail.address_beneficiary                  = address_beneficiary
        client.beneficiarydetail.phone_number_beneficiary                  = phone_number_beneficiary
        client.beneficiarydetail.bank_name_beneficiary                  = bank_name_beneficiary
        
        
        client.save()
        print('success')
        # except:
        #    print('failed')
        
        # bank details 
        
        
        # saving to bank details 
        # bank                    = BankDetail()
        # bank_obj.bank_name          = bank_name
        # bank_obj.account_number     = account_number
        # bank_obj.branch             = branch
        
        # bank.save()
        
        # Beneficiary Details
        
        
        # saving to Beneficiary Details
        
        # beneficiary              = BeneficiaryDetail()
        # beneficiary.full_name    = full_name
        # beneficiary.address_beneficiary      = address_beneficiary
        # beneficiary.phone_number_beneficiary = phone_number_beneficiary
        # beneficiary.bank_name_beneficiary    = bank_name_beneficiary
        
        # beneficiary.save()
    return render(request,'client/client.html') 

# using form control   /

def clientsave(request):
    if request.method == 'POST':
        client = ClientDetailForm(request.POST)
        bank   = BankDetailForm(request.POST)
        beneficiary = BeneficiaryDetailForm(request.POST)
        
        if client.is_valid() and bank.is_valid() and beneficiary.is_valid():
            # try:
            bankform = bank.save()
            beneficiaryform = beneficiary.save()
            clientform = client.save(commit=False)
        
            clientform.bankform     = bankform
            clientform.beneficiaryform = beneficiaryform
            clientform.save()
            print('its seems good')
            return redirect('/')
            #     print('bad')    
            
            
            
        else:
            print('bad submission')
    else:
        client = ClientDetailForm()
        bank   = BankDetailForm()
        beneficiary = BeneficiaryDetailForm()
        
    context = {
        'client':client,
        'bank':bank,
        'beneficiary':beneficiary
    }    
    return render(request,'client/formstyle.html',context)


class ClientDetailFormPreview(FormPreview):

    def done(self, request, cleaned_data):
        # Do something with the cleaned_data, then redirect
        # to a "success" page.
        
        return HttpResponseRedirect('')        