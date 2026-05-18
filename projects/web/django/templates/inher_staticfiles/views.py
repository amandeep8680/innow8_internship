from django.shortcuts import render

# Create your views here.
def base(request):
    blog = {
        "Name" :"Amandeep Singh"
    }
    return render(request,'base.html',blog)

def home(request):
    blog = {
        "Name" :"Amandeep Singh"
    }
    return render(request,'home.html',blog)

def about(request):
    blog = {
        "Name" :"Amandeep Singh"
    }
    return render(request,'about.html',blog)