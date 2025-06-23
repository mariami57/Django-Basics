from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from Regular_Exam___22_June_2025.utils import get_organizer
from event.forms import EventCreateForm, EventEditForm, EventDeleteForm
from event.models import Event


# Create your views here.
class EventsView(ListView):
    model = Event
    template_name = 'event/events.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.all().order_by('-start_time')


class EventCreateView(CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = 'event/create-event.html'
    success_url = reverse_lazy('events')

    def form_valid(self, form):
        form.instance.organizer = get_organizer()
        return super().form_valid(form)


class EventDetailView(DetailView):
    model = Event
    template_name = 'event/details-event.html'
    pk_url_kwarg = 'event_pk'


class EventEditView(UpdateView):
    model = Event
    form_class = EventEditForm
    template_name = 'event/edit-event.html'
    pk_url_kwarg = 'event_pk'

    def get_success_url(self):
        return  reverse('details-event', kwargs={'event_pk': self.object.pk})



class EventDeleteView(DeleteView):
    model = Event
    form_class = EventDeleteForm
    template_name = 'event/delete-event.html'
    pk_url_kwarg = 'event_pk'
    success_url = reverse_lazy('events')

    def get_initial(self):
        event_pk = self.kwargs.get(self.pk_url_kwarg)
        event = self.model.objects.get(pk=event_pk)
        return event.__dict__

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return  redirect(self.success_url)


