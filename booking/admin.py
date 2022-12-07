from django.contrib import admin
from booking.models import Artist

# Register your models here.
class artist_admin(admin.ModelAdmin):
    
    readonly_fields=("created","updated")


admin.site.register(Artist, artist_admin)

