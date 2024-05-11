from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    # dest1 = Destination()
    # dest1.name = 'Canada '
    # dest1.desc = 'This country is very cool in its envireonment'
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 432
    # dest1.offer = True
    
    # dest2 = Destination()
    # dest2.name = 'Tanzania '
    # dest2.desc = 'This country of very humble men'
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 344
    # dest2.offer = False

    # dest3 = Destination()
    # dest3.name = 'Soudi arabia '
    # dest3.desc = 'This country where arabian are living for so long in Bussiness '
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 498
    # dest3.offer = True

    # dests = [dest1,dest2,dest3]

    dests = Destination.objects.all()
    return render(request, "index.html", {'dests':dests})


