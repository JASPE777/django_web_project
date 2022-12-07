from django.db import models

# Create your models here.
class Artist(models.Model):
    name=models.CharField(max_length=50)
    picture=models.ImageField(blank=True, null=True, upload_to='booking/artists', default='booking/sin_imagen.png')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    instagram = models.URLField(max_length=80)
    soundcloud = models.URLField(max_length=80)
    bio=models.CharField(max_length=1000)



    class meta:

        verbose_name="Artist"
        verbose_name_plural="Artists"