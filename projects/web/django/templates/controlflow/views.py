from django.shortcuts import render
from datetime import datetime
# Create your views here.
def control(request):
    blogs=[
            { "title":"Django Basics","is_featured":True,"author":"Aman"},
            { "title":"Django advanced","is_featured":False,"author":""},
            {"title":"Django Frameworks","is_featured":True,"author":"deep"},

        
    ]


    context={
        "blogs": blogs,
        "today":datetime.now(),
        "html_code":"<h1>Welcome Bro</h1>",
    }
    return render(request,'control.html',context)