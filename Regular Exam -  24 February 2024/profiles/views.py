from django.db.models.aggregates import Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from DjangoProject.utils import get_profile
from profiles.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from profiles.models import Profile



# Create your views here.
class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profile/profile-details.html"

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        total_cost = self.object.cars.aggregate(total=Sum('price'))['total'] or 0

        kwargs.update({'total_cost': total_cost})
        return super().get_context_data(**kwargs)
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = "profile/profile-create.html"
    success_url = reverse_lazy('car-catalogue')



class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = "profile/profile-edit.html"
    success_url = reverse_lazy('details-profile')

    def get_object(self, queryset=None):
        return get_profile()

class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = "profile/profile-delete.html"
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)