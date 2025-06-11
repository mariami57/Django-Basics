from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from common.forms import CommentForm, SearchForm
from pets.models import Pet
from photos.models import Photo
from common.models import Like


# Create your views here.
def home_page_view(request):

    all_photos = Photo.objects.prefetch_related('tagged_pets', 'like_set').all()
    comment_form = CommentForm()
    search_form = SearchForm(request.GET or None)

    if search_form.is_valid():
        all_photos=(Photo.objects.prefetch_related('tagged_pets', 'like_set')
                     .filter(tagged_pets__name__icontains=search_form.cleaned_data.get('text','')))
    else:
        all_photos = Photo.objects.prefetch_related('tagged_pets', 'like_set').all()

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
    }

    return render(request, 'common/home-page.html', context)

def like_functionality(request, photo_id:int):
    liked_photo = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_photo:
        liked_photo.delete()
    else:
        Like.objects.create(
            to_photo_id=photo_id,
        )
    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')

def share(request, photo_id:int):
    copy(request.META.get('HTTP_HOST') + resolve_url('details_photo', photo_id))

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')

def add_comment(request, photo_id:int):
    form = CommentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.to_photo = Photo.objects.get(pk=photo_id)
        comment.save()

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')