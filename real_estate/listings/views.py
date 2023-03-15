from django.shortcuts import render
from .models import Listing

def listing_list(request):
    listings = Listing.objects.all()
    context = {
        'listings' : listings
    }
    return render(request, 'listings.html', context)