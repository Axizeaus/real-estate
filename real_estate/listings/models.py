from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    num_bedroom = models.IntegerField()
    num_bathroom = models.IntegerField()
    sqft = models.IntegerField()
    address = models.CharField(max_length=100)
    # image
    
    def __str__(self):
        return self.title