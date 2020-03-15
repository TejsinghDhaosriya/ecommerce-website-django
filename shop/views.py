from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'shop/index.html')

    #return HttpResponse("myblog") 
def tacker(request):
    return HttpResponse("we are at tracker")

def search(request):
    return HttpResponse("we are at search")

def contact(request):
    return HttpResponse("we are at contatus")

def productview(request):
    return HttpResponse("we are at prdv")

def about(request):
    return HttpResponse("we are at about")

def tracker(request):
    return HttpResponse("we are at tacker")
def checkout(request):
    return HttpResponse("we are at checker")