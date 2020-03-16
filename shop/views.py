from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    products=(Product.objects.all())
    n=len(products)
    nSlides=n//4 + ceil((n/4) -(n//4))
    #params={'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    allProds=[[products,range(1,nSlides),nSlides],
              [products,range(1,nSlides),nSlides]]
    params={'allProds':allProds}
    return render(request,'shop/index.html',params)

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
    #return HttpResponse("we are at about")
    return render(request,'shop/about.html')
def tracker(request):
    return HttpResponse("we are at tacker")
def checkout(request):
    return HttpResponse("we are at checker")