from django.shortcuts import render

from trip.models import Trip


# Create your views here.
def index(request):
    return render(request, "index.html")

def all_trips_view(request):
    trips = Trip.objects.all()

    context = {
        "trips": trips,
    }

    return render(request, "all-trips.html", context)