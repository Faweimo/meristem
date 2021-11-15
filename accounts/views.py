from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
# Create your views here.
# def login(request):
    
#     return render(request,'accounts/index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'You are now logged in')
            return redirect('meristaff')


        else:
            messages.error(request,'Invalid email and password')
            return redirect('login')

    else:

                
        return render(request, 'accounts/login.html')    


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out.')
    return redirect('home')
    
            