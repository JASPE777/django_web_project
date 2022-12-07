from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Product
from django.db.models import F, Sum, FloatField


User=get_user_model()


class Orders(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    @property
    def total(self):
        return self.line_order.aggregate(

            total=Sum(F('price')*F('amount'), output_field=FloatField())

        )['total']


    class Mete:

        db_table='Pedidos'
        verbos_name='Pedido'
        verbos_name_plural='Pedidos'
        ordering='id'

class Line_order(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    order=models.ForeignKey(Orders, on_delete=models.CASCADE)
    amount=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f'{self.amount} unidades de {self.product.name}'

    class Mete:
    
        db_table='LineaPedidos'
        verbos_name='Linea Pedido'
        verbos_name_plural='Lineas Pedidos'
        ordering='id'




