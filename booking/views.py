from django.shortcuts import render
from booking.models import Artist

# Create your views here.

def booking(request):
    
    artists = Artist.objects.all()
    return render(request, 'booking/booking.html', {"artists": artists})