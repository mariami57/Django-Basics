from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, FormView

from Retake_Exam___13_December_2024.utils import get_traveler
from traveler.forms import TravelerCreateForm, TravelerDeleteForm, TravelerEditForm
from traveler.models import Traveler


# Create your views here.
def traveler_details_view(request):
    traveler = Traveler.objects.first()
    trips = traveler.trips.order_by('-start_date')
    has_trips = trips.exists()

    context = {
        'traveler': traveler,
        'trips': trips,
        'has_trips': has_trips,
    }
    return render(request, "details-traveler.html", context )

class TravelerCreateView(CreateView):
    model = Traveler
    form_class = TravelerCreateForm
    template_name = "create-traveler.html"
    success_url = reverse_lazy("all_trips")

class TravelerEditView(UpdateView):
    model = Traveler
    form_class = TravelerEditForm
    template_name = "edit-traveler.html"
    success_url = reverse_lazy("traveler_details")

    def get_object(self, queryset=None):
        return get_traveler()

class TravelerDeleteView(DeleteView):
    model = Traveler
    template_name = "delete-traveler.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_traveler()
