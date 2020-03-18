from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil
# Create your views here.
def index(request):

    products=(Product.objects.all())
    #n=len(products)
    #nSlides=n//4 + ceil((n/4) -(n//4))
    #params={'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    # allProds=[[products,range(1,nSlides),nSlides],
    #           [products,range(1,nSlides),nSlides]]
    
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

    #return HttpResponse("myblog") 
def tacker(request):
    return render(request,'shop/tracker.html')
def search(request):
    return render(request,'shop/search.html')

def contact(request):
    if request.method==    "POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        print(name)
    return render(request,'shop/contact.html')

def productview(request):
    return render(request,'shop/productview.html')

def about(request):
    #return HttpResponse("we are at about")
    return render(request,'shop/about.html')
def tracker(request):
    return render(request,'shop/tracker.html')
def checkout(request):
    return render(request,'shop/checkout.html')
    #return HttpResponse("we are at checker")