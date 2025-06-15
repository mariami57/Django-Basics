

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView

from cars.forms import CarCreateForm, CarEditForm, CarDeleteForm
from cars.models import Car
from profiles.models import Profile


# Create your views here.
class CarCatalogueView(ListView):
    model = Car
    template_name = "cars/catalogue.html"

class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = "cars/car-create.html"
    success_url = reverse_lazy('car-catalogue')

    def form_valid(self, form):
        owner = Profile.objects.first()
        form.instance.owner = owner
        return super().form_valid(form)

class CarEditView(UpdateView):
    model = Car
    form_class = CarEditForm
    template_name = "cars/car-edit.html"
    success_url = reverse_lazy('car-catalogue')

class CarDeleteView(DeleteView, FormView):
    model = Car
    form_class = CarDeleteForm
    template_name = "cars/car-delete.html"
    success_url = reverse_lazy('car-catalogue')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        car = self.model.objects.get(pk=pk)
        return car.__dict__

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)

class CarDetailView(DetailView):
    model = Car
    template_name = "cars/car-details.html"

