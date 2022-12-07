from django.shortcuts import render
from tienda.models import Product

# Create your views here.

def tienda(request):
    
    products = Product.objects.all()
    return render(request, 'tienda/tienda.html', {"products": products})
