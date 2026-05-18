from django.shortcuts import render

# Create your views here.
def temp1(request):
    return render(request,'home.html')