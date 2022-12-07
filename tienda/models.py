from django.db import models

# Create your models here.

class category_prod(models.Model):

    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name="categoryprod"
        verbose_name_plural="categoryprod"

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(category_prod, on_delete=models.CASCADE)
    picture=models.ImageField(blank=True, null=True, upload_to='tienda/products', default='tienda/sin_imagen.png')
    price=models.FloatField()
    availability=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class meta:

        verbose_name="product"
        verbose_name_plural="products"
