from django.shortcuts import render, redirect

from SoftUni_Petstagram.main_app.forms import CreatePetForm
from SoftUni_Petstagram.main_app.helpers import get_profile
from SoftUni_Petstagram.main_app.models import Profile, PetPhoto, Pet


def add_pet(request):
    instance = Pet(owner=get_profile())
    if request.method == 'POST':
        form = CreatePetForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CreatePetForm(instance=instance)
    return render(request, 'pet_create.html', {'form': form})


def edit_pet(request):
    return render(request, 'pet_edit.html')


def delete_pet(request):
    return render(request, 'pet_delete.html')
