from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, FormView

import post
from author.models import Author
from post.forms import PostCreateForm, PostEditForm, PostDeleteForm
from post.models import Post


# Create your views here.
class PostCreate(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = "post/create-post.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        author_profile = Author.objects.first()

        post = form.save(commit=False)
        post.author = author_profile
        post.save()

        return super().form_valid(form)


class PostDetail(DetailView):
    model = Post
    template_name = "post/details-post.html"

class PostEdit(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = "post/edit-post.html"
    success_url = reverse_lazy("dashboard")

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post=self.model.objects.get(pk=pk)
        return post.__dict__


class PostDelete(DeleteView, FormView):
    model = Post
    form_class = PostDeleteForm
    template_name = "post/delete-post.html"
    success_url = reverse_lazy("dashboard")

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = self.model.objects.get(pk=pk)
        return post.__dict__

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)

