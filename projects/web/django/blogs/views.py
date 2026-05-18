from django.shortcuts import render
from django.http import HttpResponse




def names(request):
    return HttpResponse("<h1>This is vlog page bro</h1>")
