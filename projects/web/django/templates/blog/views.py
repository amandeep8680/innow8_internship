from django.shortcuts import render
from datetime import  datetime

# Create your views here.

class User:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

def home(request):
    context = {
        "name":"Amandeep Singh",
        "age":23,
        "skills" : ["python","django","React"],
        "user" : User("Singh",30),
        "blog" : {
            "title" : "django template intro",
            "content":"<b>This is bold</b>",
            "created_at" : datetime(2026,3,10,15,30)
        },
        "empty_value" : None,
    }
    return render(request,"home.html",context)
