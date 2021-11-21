from django.shortcuts import render,redirect
from django.http import HttpResponse
from example.models import Client
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView, 
    UpdateView,
    DeleteView
)
from .forms import ClientForm
from accounts.models import User
from client.models import ClientDetail
# Create your views here.
def index(request):
    if not request.user.user_type == 1:
        return HttpResponse('You are not allow to view this page')
    else:
        
        clients = ClientDetail.objects.all()
        paginator               = Paginator(clients,25)
        page                    = request.GET.get('page')
        paged_clients           = paginator.get_page(page)
        context = {
            'clients':paged_clients
        }
    return render(request,'example/index.html',context)

# create view 
def create(request):
    if request.method == 'POST':
        clientform = ClientForm(request.POST or  None)
        if clientform.is_valid():
            clientform.save()
            messages.success(request,'You have successfully submit your crendentials')
            return redirect('create')
            
        else:
            print('failed')    
    else:
        clientform = ClientForm()        
    context = {
        'clientform':clientform
    }        
    return render(request,'example/create.html',context)
    
# search fields   /
def search(request):
    if not request.user.user_type == 1:
        return HttpResponse('You are not allow to view this page')
    else: 
        # keyword
        if 'keyword' in request.GET:
            keyword     = request.GET['keyword']
            if keyword:
                clients = ClientDetail.objects.all().order_by('-updated_at').filter(Q(first_name__icontains=keyword )|Q(last_name__icontains=keyword))
                paginator               = Paginator(clients,25)
                page                    = request.GET.get('page')
                paged_clients           = paginator.get_page(page)
                total                   = clients.count()
              
            context = {
                'clients':paged_clients,
                'total':total
            
            }   
        return render(request,'example/index.html',context)

# deleting client  /
def delete(request,delete_id):
    
    
        
    if not request.user.user_type == 1:
        return HttpResponse('You are not allow to view this page')
    
    
    else:
        client  = ClientDetail.objects.get(id=delete_id)
        if request.method == 'POST':
            client.delete()
            messages.success(request,'Client deleted successfully')
            return redirect('example')
        context = {
            'client':client,
        }
    return render(request,'example/delete.html',context)


# for editing and updating client details
def edit(request,edit_id):
    if not request.user.user_type == 1:
        return HttpResponse('You are not allow to vie this page')
    else:
        client_obj = ClientDetail.objects.get(id=edit_id)
        if request.method == 'POST':
            clientform = ClientForm(request.POST or None, instance=client_obj)
            # validating the form 
            if clientform.is_valid():
                clientform.save()
                messages.success(request,'Client updated successfully')
                return redirect('example')
            else:
                messages.error(request,'Failed to update client')
        else:
            clientform = ClientForm(instance=client_obj)     
        context = {
            'clientform':clientform
        }       
        return render(request,'example/edit.html',context)
            
            