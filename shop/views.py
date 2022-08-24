from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
from math import ceil
# Create your views here.
def index(request):
    products=Product.objects.all()
    n=len(products)
    nSlides= n//4 + ceil((n/4)-(n//4))
    # context={'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    allproducts=[[products,range(1,len(products)),nSlides],
    [products,range(1,len(products)),nSlides]]
    context={'allproducts':allproducts}
    return render(request,'shop/index.html',context)
