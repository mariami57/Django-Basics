from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, FormView, ListView
from django.views.generic.edit import FormMixin

from Exam_Prep_I.utils import get_profile
from albums.models import Album
from profiles.forms import ProfileCreateForm


# Create your views here.

class HomeView(ListView, FormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        if get_profile():
            return ['common/home-with-profile.html']
        else:
            return ['common/home-no-profile.html']

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)
