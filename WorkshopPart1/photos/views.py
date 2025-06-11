from django.shortcuts import render, redirect

from common.forms import CommentForm
from photos.forms import PhotoCreateForm, PhotoEditForm
from photos.models import Photo


# Create your views here.
def add_photo_view(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form': form,
    }



    return render(request, 'photos/photo-add-page.html', context)

def details_photo_view(request, pk:int):
    photo = Photo.objects.prefetch_related('comment_set').get(pk=pk)
    comments = photo.comment_set.all()
    comment_form = CommentForm()

    context = {
        'photo': photo,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'photos/photo-details-page.html', context)

def edit_photo_view(request, pk:int):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, request.FILES or None, instance=photo)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'photo': photo,
        'form': form,
    }
    return render(request, 'photos/photo-edit-page.html', context)


def photo_delete_view(request, pk:int):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home')