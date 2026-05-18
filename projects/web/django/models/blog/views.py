from django.shortcuts import render
from .models import Student


# Create your views here.
def show(request):
    student = Student.objects.all()
    return render(request,'web.html',{'students': student})