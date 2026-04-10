from django.shortcuts import render ,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Login Successfully")
            return redirect('dashboard')
        else:
            messages.error(request,"Login Failed")
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form})

 
def login_view(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None: 
            login(request,user)
            messages.success(request,"Login Successfully")
            return redirect('dashboard')
        else:
            messages.error(request,"Login Failed")
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    messages.success(request,'Logout Successfull')
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render (request,'dashboard.html')