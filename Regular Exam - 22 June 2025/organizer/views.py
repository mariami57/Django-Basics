from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from Regular_Exam___22_June_2025.utils import get_organizer
from event.models import Event
from organizer.forms import OrganizerCreateForm, OrganizerEditForm
from organizer.models import Organizer


# Create your views here.
class OrganizerCreateView(CreateView):
    model = Organizer
    form_class = OrganizerCreateForm
    template_name = 'organizer/create-organizer.html'
    success_url = reverse_lazy('events')


class OrganizerDetailView(DetailView):
    model = Organizer
    template_name = 'organizer/details-organizer.html'

    def get_object(self, queryset=None):
        return get_organizer()

    def get_queryset(self):
        events = Event.objects.filter(start_time__gt=timezone.now()).order_by('start_time')
        return events
    
    def get_context_data(self, **kwargs):
        kwargs.update({
            'events': self.get_queryset()
        })
        return super().get_context_data(**kwargs)

class OrganizerEditView(UpdateView):
    model = Organizer
    form_class = OrganizerEditForm
    template_name = 'organizer/edit-organizer.html'
    success_url = reverse_lazy('organizer_details')

    def get_object(self, queryset=None):
        return get_organizer()


class OrganizerDeleteView(DeleteView):
    model = Organizer
    template_name = 'organizer/delete-organizer.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_organizer()

    def get_queryset(self):
        events = Event.objects.filter(start_time__gt=timezone.now()).order_by('start_time')
        return events

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not self.get_queryset().exists():
            self.object.delete()

        return redirect(self.success_url)
