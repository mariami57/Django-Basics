from django.shortcuts import render

# Create your views here.
def add_pet_view(request):
    return render(request, 'pets/pet-add-page.html')

def delete_pet_view(request, username:str, pet_slug:str):
    return render(request, 'pets/pet-delete-page.html')

def edit_pet_view(request, username:str, pet_slug:str):
    return render(request, 'pets/pet-edit-page.html')

def details_pet_view(request, username:str, pet_slug:str):
    return render(request, 'pets/pet-details-page.html')