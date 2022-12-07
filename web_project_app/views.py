from django.shortcuts import render, HttpResponse
from shopping_cart.cart import Cart




def home(request):

    cart=Cart(request)
    
    return render(request, 'web_project_app/home.html')




def cv(request):
    
    return render(request, 'web_project_app/cv.html')



def musica(request):
    
    return render(request, 'web_project_app/musica.html')



