from orders.models import Product
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from orders.models import Line_order, Orders
from shopping_cart.cart import Cart
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from validation.forms import User, UserForm



@login_required(login_url="/validation/logear")
def process_order(request):

    order=Orders.objects.create(user=request.user)
    cart=Cart(request)
    line_order=list()
    for key, value in cart.cart.items():
        line_order.append(Line_order(
        
            product_id=key,
            amount=value["amount"],
            user=request.user,
            order=order
            ))

    Line_order.objects.bulk_create(line_order)

    send_email(
        
        order=order,
        line_order=line_order,
        name_user=request.user.username,
        email_user=request.user.email
    
    
    )

    messages.success(request, "Pedido enviado con exito")


    return redirect("/")

def send_email(**kwargs):

    subject="Gracias por hacer tu pedido."
    message_m=render_to_string("emails/order.html",{
        "order": kwargs.get("order"),
        "line_order": kwargs.get("line_order"),
        "name_user": kwargs.get("name_user"),


    })

    message_text=strip_tags(message_m)
    from_email="95schunk@gmail.com"
    to=kwargs.get('email_user')
    # to='yojuanmaa@hotmail.com'

    send_mail(subject, message_text, from_email, [to], html_message=message_m)

