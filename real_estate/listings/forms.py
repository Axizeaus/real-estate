from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):
    class Meta: 
        model = Listing
        fields = [
            'title', 
            'price',
            'num_bedroom',
            'num_bathroom', 
            'sqft',
            'address',
            'image',
        ]
    
