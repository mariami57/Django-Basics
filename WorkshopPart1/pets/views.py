from django.shortcuts import render, redirect

from common.forms import CommentForm
from pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from pets.models import Pet


# Create your views here.
def add_pet_view(request):
    form = PetCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)

    context = {
        'form': form,
    }
    return render(request, 'pets/pet-add-page.html', context)

def delete_pet_view(request, username:str, pet_slug:str):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetDeleteForm(instance=pet)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pets/pet-delete-page.html',context)

def edit_pet_view(request, username:str, pet_slug:str):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('details_pet', username=username, pet_slug=pet_slug)

    context = {
        'form': form,
        'pet': pet,
    }


    return render(request, 'pets/pet-edit-page.html', context)

def details_pet_view(request, username:str, pet_slug:str):
    pet = Pet.objects.get(slug=pet_slug)
    comment_form = CommentForm()

    all_photos = pet.photo_set.prefetch_related('tagged_pets', 'like_set').all()

    context ={
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
    }
    return render(request, 'pets/pet-details-page.html', context)