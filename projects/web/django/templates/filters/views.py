from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from . import views
# Create your views here.

def home(request):
    return HttpResponse("Hi")


def blog_details(request):
    post ={
        "title":"My secend template",
        "desc":"hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",
        "author":"yes",
        "comment_count":77,
        "created_at" : datetime(2026,3,10,15,30),
        "tags":["python","django","React"],
        "price":500,
        "number":3
    }
    return render(request,"blog_detail.html",{"Post":post})


