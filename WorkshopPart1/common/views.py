from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from pets.models import Pet
from photos.models import Photo
from common.models import Like


# Create your views here.
def home_page_view(request):

    all_photos = Photo.objects.prefetch_related('tagged_pets', 'like_set').all()

    context = {
        'all_photos': all_photos,
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
