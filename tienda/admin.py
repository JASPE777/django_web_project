from django.contrib import admin
from tienda.models import category_prod, Product

# Register your models here.
class category_prod_admin(admin.ModelAdmin):
    
    readonly_fields=("created","updated")

class product_admin(admin.ModelAdmin):

    readonly_fields=("created","updated")

admin.site.register(category_prod, category_prod_admin)
admin.site.register(Product, product_admin)