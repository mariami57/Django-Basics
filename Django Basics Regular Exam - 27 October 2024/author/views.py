from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from author.forms import AuthorBaseForm, AuthorCreateForm, AuthorEditForm
from author.models import Author
from common.utils import get_author


# Create your views here.
class AuthorDetails(DetailView):
    model = Author
    template_name = "author/details-author.html"

    def get_object(self, queryset = None):
        return get_author()


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = "author/create-author.html"
    success_url = reverse_lazy('dashboard')


class AuthorEdit(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = "author/edit-author.html"
    success_url = reverse_lazy('author-details')

    def get_object(self, queryset = None):
        return get_author()


class AuthorDelete(DeleteView):
    model = Author
    template_name = "author/delete-author.html"
    success_url = reverse_lazy('index')

    def get_object(self, queryset = None):
        return get_author()

