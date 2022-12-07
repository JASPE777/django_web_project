from django.contrib import admin

from .models import Orders, Line_order


admin.site.register([Orders, Line_order])
