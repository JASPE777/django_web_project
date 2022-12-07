from django.shortcuts import render, redirect
from .forms import formulario_contacto
from django.core.mail import EmailMessage



def contacto(request):

    form_contacto = formulario_contacto()

    if request.method=="POST":

        form_contacto = formulario_contacto(data=request.POST)
        if form_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            telefono=request.Post.get("telefono")
            mensaje=request.POST.get("mensaje")

            email=EmailMessage("Mensaje desde App Contacto",
             "El usuario: {} , con la dirección {}, escribe lo siguiente:\n\n {}".format(nombre,email,telefono,mensaje),"",
             ['95schunk@gmail.com'],reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido")

            except:

                return redirect("/contacto/?novalido")  

    return render(request, "contacto/contacto.html", {'miformulario':formulario_contacto})