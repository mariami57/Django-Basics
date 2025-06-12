from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, FormView

from traveler.forms import TravelerCreateForm, TravelerDeleteForm
from traveler.models import Traveler


# Create your views here.
def traveler_details_view(request, pk):
    traveler = Traveler.objects.get(pk=pk)

    context = {
        'traveler': traveler,
    }
    return render(request, "details-traveler.html", context )

class TravelerCreateView(CreateView):
    model = Traveler
    form_class = TravelerCreateForm
    template_name = "create-traveler.html"
    success_url = reverse_lazy("all_trips")

class TravelerEditView(UpdateView):
    model = Traveler
    form_class = TravelerCreateForm
    template_name = "edit-traveler.html"
    success_url = reverse_lazy("index")

class TravelerDeleteView(DeleteView):
    model = Traveler
    form_class = TravelerDeleteForm
    template_name = "delete-traveler.html"
    success_url = reverse_lazy("index")

