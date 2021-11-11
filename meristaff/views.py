from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from client.models import *
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

@login_required
def index(request):
    if not request.user.user_type == 1:
        return HttpResponse('You are not allow to view this page')
    else:
        
        client  = ClientDetail.objects.all()
        bank    = BankDetail.objects.all()
        paginator               = Paginator(client,25)
        page                    = request.GET.get('page')
        paged_employees         = paginator.get_page(page)
    context = {
        'client':paged_employees,
        
        
    }
    return render(request,'meristaff/index.html',context)

# for editing and updating client models or details 

def edit_clientdetails(request,client_id):
    if not request.user.user_type == 1:
        return HttpResponse('You are not allow to view this page')
    else:
        client   = ClientDetail.objects.all()
        context  = {
            'id':client_id,
            'client':client
        }
        return render(request,'meristaff/edit_staff.html',context)
    
def edit_client_save(request):
    if not request.user.user_type == 1:
        return HttpResponse('You are not allow to view this page')
    else:
         # Client Details
        client_id               = request.POST['client_id']
        title                   = request.POST['title']
        first_name              = request.POST['first_name']
        surname                 = request.POST['surname']
       
        
        
        bank_name               = request.POST['bank_name']
        
        
        full_name               = request.POST['full_name']
        
        
        try:
            client = ClientDetail.objects.get(id=client_id)
            client.title = title
            client.first_name = first_name
            client.surname = surname
            client.save()
            
            bank = BankDetail.objects.get(id=client_id)
            bank.bank_name = bank_name
            bank.save()
            
            beneficiary         = BeneficiaryDetail.objects.get(id=client_id)
            beneficiary.full_name = full_name
            beneficiary.save()
            print('success')
            return redirect('meristaff')
            
        except:
            print('bad')    


def delete_client(request,client_id):
    if not request.user.user_type == 1:
        return HttpResponse('You are not allow to view this page')        
    else:
        name = request.GET.get('name')
        
        client = ClientDetail.objects.get(id=client_id)
        
        if request.method == 'POST':
            client.delete()
            return redirect('meristaff')
        
        context = {
            'client':client_id
        }
        return render(request,'meristaff/delete_client.html',context)
        
        
        