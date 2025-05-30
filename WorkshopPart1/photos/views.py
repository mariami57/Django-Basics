from django.shortcuts import render

# Create your views here.
def add_photo_view(request):
    return render(request, 'photos/photo-add-page.html')

def details_photo_view(request, pk:int):
    return render(request, 'photos/photo-details-page.html')

def edit_photo_view(request, pk:int):
    return render(request, 'photos/photo-edit-page.html')