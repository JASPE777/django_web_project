def amount_total_cart(request):
    total=0
    if request.user.is_authenticated:
        for key, value in request.session["cart"].items():
            total=total+float(value["price"])

    else:

        total="Debes iniciar sesión"
    
    return {"amount_total_cart":total}