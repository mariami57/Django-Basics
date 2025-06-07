from datetime import datetime

from django.db.models.query_utils import Q
from django.forms.models import modelform_factory
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from posts.forms import PostBaseForm, PostCreateForm, PostEditForm, PostDeleteForm, SearchForm, CommentForm, \
    CommentFormSet
from posts.models import Post


# Create your views here.
def index(request):
    return render(request, "index.html")

def dashboard(request):
    search_form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == "GET" and search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        posts = posts.filter(Q(title__icontains=query) |
                             Q(content__icontains=query) |
                             Q(author__icontains=query))

    if request.method == "POST":
        return redirect('index')

    context = {
            "posts": posts,
            "search_form": search_form,
        }

    return render(request, "posts/dashboard.html", context)

def add_post(request):
    form = PostCreateForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {"form": form}

    return render(request, "posts/add_post.html", context)

def edit_post(request, pk:int):
    post = Post.objects.get(pk=pk)

    if request.user.is_superuser:
        PostEditForm = modelform_factory(Post, fields='__all__')
    else:
        PostEditForm = modelform_factory(Post, fields=('content',))

    form = PostEditForm(request.POST or None, instance=post)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {"form": form}
    return render(request, "posts/edit_post.html", context)

def post_details(request, pk):

    post = Post.objects.get(pk=pk)
    comment_form_set = CommentFormSet(request.POST or None)

    if request.method == "POST" and comment_form_set.is_valid():
        for form in comment_form_set:
            comment = form.save(commit=False)
            comment.author = request.user.username
            comment.post = post
            comment.save()
            return redirect('details_post', pk=post.pk)


    context = {
        "post": post,
        "formset": comment_form_set,
    }

    return render(request, "posts/details_post.html", context)

def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    if request.method == "POST":
        post.delete()
        return redirect('dashboard')

    context = {
        "form": form,
    }

    return render(request, "posts/delete_post.html", context)