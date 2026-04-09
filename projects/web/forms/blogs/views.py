from django.shortcuts import render , redirect
from .models import Info
from django.http import HttpResponse

# Create your views here.
def contact(request):
    return render(request,'form.html',)

def submit(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        messege=request.POST.get('messege')



        if name and messege:
            Info.objects.create(name=name,age=age,messege=messege)
            # return HttpResponse(f"Thanks {name} for submitting the form")
            return redirect(contact)
        
        
        else:
            HttpResponse("Provide both name and messege")

    return redirect(contact)
