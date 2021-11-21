from django.shortcuts import redirect, render
from django.http import HttpResponse

from client.models import ClientDetail
# Create your views here.
from .forms import ClientDetailForm
        
# import generic FormView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect



 
'''
for updating and deleting from the staff page(FRONTEND) pls got to the EXAMPLE app in 
the views.py AND MAKE USE OF THE TEMPLATES IN THE EXAMPLE APP AND URL

all works are done completely in client app and example app and their templates dont go more than 
this app
'''



# using form control   /

def clientsave(request):
    if request.method == 'POST':
        
        client      = ClientDetailForm(request.POST or None)
        # return HttpResponse('not post method')
    
        if client.is_valid():
           
            client.save()
            print('its seems good')
            return redirect('/')
            
        else:
            print('bad submission')
    else:
        client      = ClientDetailForm()
        
    context = {
        'client':client,
       
    }    
    return render(request,'client/formstyle.html',context)
'''

u can check this reference templates  but first template(formstyle.html) used in this view is not styles but is working
perfectly, u can use this template(formstyle.html) to edit whatever templates u want to use

 these are not complete functioning
return render(request,'client/cli.html',context)
return render(request,'client/stylex.html',context)

'''





