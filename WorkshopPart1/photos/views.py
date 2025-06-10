from django.shortcuts import render

from photos.models import Photo


# Create your views here.
def add_photo_view(request):
    return render(request, 'photos/photo-add-page.html')

def details_photo_view(request, pk:int):
    photo = Photo.objects.prefetch_related('comment_set').get(pk=pk)
    comments = photo.comment_set.all()

    context = {
        'photo': photo,
        'comments': comments,
    }

    return render(request, 'photos/photo-details-page.html', context)

def edit_photo_view(request, pk:int):
    return render(request, 'photos/photo-edit-page.html')