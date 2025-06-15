import profile

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from author.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from author.models import Profile


# Create your views here.
class CreateAuthor(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = "profile/create-profile.html"
    success_url = reverse_lazy('recipe-catalogue')

class DetailsAuthor(DetailView):
    model = Profile
    template_name = "profile/details-profile.html"

    def get_object(self, queryset=None):
        return Profile.objects.first()


class EditAuthor(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = "profile/edit-profile.html"
    success_url = reverse_lazy('detail-author')

    def get_object(self, queryset=None):
        return Profile.objects.first()

class DeleteAuthor(DeleteView):
    model = Profile
    template_name = "profile/delete-profile.html"
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)