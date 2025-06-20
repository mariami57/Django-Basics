from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from Exam_Prep_I.utils import get_profile
from albums.forms import CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from albums.models import Album


# Create your views here.
class CreateAlbumView(CreateView):
    model = Album
    form_class = CreateAlbumForm
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_profile()
        return super().form_valid(form)

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'albums/album-details.html'
    pk_url_kwarg = 'id'


class AlbumEditView(UpdateView):
    model = Album
    form_class = EditAlbumForm
    template_name = 'albums/album-edit.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

class AlbumDeleteView(DeleteView):
    model = Album
    form_class = DeleteAlbumForm
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def get_initial(self):
        id = self.kwargs.get(self.pk_url_kwarg)
        album = self.model.objects.get(id=id)
        return album.__dict__

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


