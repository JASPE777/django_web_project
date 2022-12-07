from django.shortcuts import render, redirect
from .cart import Cart
from tienda.models import Product


def add_product(request, product_id):
    cart=Cart(request)
    product=Product.objects.get(id=product_id)
    cart.add_product(product=product)
    return redirect("tienda")

def delete_product(request, product_id):
    cart=Cart(request)
    product=Product.objects.get(id=product_id)
    cart.delete_product(product=product)
    return redirect("tienda")

def subtract_product(request, product_id):
    cart=Cart(request)
    product=Product.objects.get(id=product_id)
    cart.subtract_product(product=product)
    return redirect("tienda")

def clean_cart(request, product_id):
    cart=Cart(request)
    cart.clean_cart()

    return redirect("tienda")



# Create your views here.
