from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as login_proccess
from django.contrib import messages
from validation.forms import UserForm



class V_register(View):

    def get(self, request):
        
        form=UserForm()
        return render(request, "register/register.html",{"form":form}) 

    def post(self, request):
        form=UserForm(request.POST)

        if form.is_valid():
            
            user=form.save()

            login_proccess(request, user)

            return redirect('home')

        else: 
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request, "register/register.html",{"form":form}) 

def close_acount(request):

    logout(request)

    return redirect('home')


def login(request):

    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contrasena=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contrasena)
            if usuario is not None:
                login_proccess(request, usuario)
                return redirect('home')

            else:
                messages.error(request, "usuario invalido")

        else:
            messages.error(request, "Informacion incorrecta")


    form=AuthenticationForm()
    return render(request,"login/login.html",{"form":form}) 




