from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome AMAN")

def sum(request):
    return HttpResponse(10+20)




# -=-=---==-=-=-===-=-=-=-=--=-=-=-=-=-=  url parameter =-=-=-==-=-=-==-=-=-==-=-=- 


# using path 

def parameter_path(request,user_id):
    return HttpResponse(f"Hi' Your parameterized url with path is {user_id}.")
# //multiple

def parameter_pathh(request,user_name,user_ids):
    return HttpResponse(f"<h1>Hi {user_name} your id is {user_ids}</h1>")


# using re_path(Regex Path)
# used for expressions complex patterns when need string,symbol,numbers

def re_path(request,year):
    return HttpResponse(f"Hi' Your re_path url with path is {year}.")

def re_path1(request,bro_id):
    return HttpResponse(f"Hi,your regex link is: {bro_id}")






# using **kwargs

def details(request , **kwargs):
    return HttpResponse(f"Hi your details are Name: {kwargs['username']} and Age is {kwargs['age']}")


# if one argu is missing


def detailss(request , **kwargs):
    name =kwargs.get('username','Guest')
    age = kwargs.get('age',23)
    return HttpResponse(f"Hi your details are Name: {name} and Age is {age}")

