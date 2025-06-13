from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, FormView

from traveler.models import Traveler
from trip.forms import TripCreateForm, TripDeleteForm
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

class TripCreateView(CreateView):
    model = Trip
    form_class = TripCreateForm
    success_url = reverse_lazy("all_trips")
    template_name = "create-trip.html"

    def form_valid(self, form):
        traveler_profile= Traveler.objects.first()

        trip = form.save(commit=False)
        trip.traveler = traveler_profile
        trip.save()

        return super().form_valid(form)

class TripEditView(UpdateView):
    model = Trip
    form_class = TripCreateForm
    success_url = reverse_lazy("all_trips")
    template_name = "edit-trip.html"

class TripDeleteView(DeleteView,FormView):
    model = Trip
    form_class = TripDeleteForm
    success_url = reverse_lazy("all_trips")
    template_name = "delete-trip.html"

    def get_intial(self):
        pk =self.kwargs.get(self.pk_url_kwarg)
        trip=self.model.objects.get(pk=pk)
        return trip.__dict__

def trip_details(request, pk):
    trip = Trip.objects.get(pk=pk)

    context = {
        "trip": trip,
    }

    return render(request, "details-trip.html", context)