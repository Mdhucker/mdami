from django.db import models

# Create your models here.

class Destination(models.Model): #actually this  is not class but is model used for database
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer = models.BooleanField(default=False)



