from django.shortcuts import render, redirect

from SoftUni_Petstagram.main_app.helpers import get_profile
from SoftUni_Petstagram.main_app.models import Profile, PetPhoto, Pet


def add_pet(request):
    return render(request, 'pet_create.html')


def edit_pet(request):
    return render(request, 'pet_edit.html')


def delete_pet(request):
    return render(request, 'pet_delete.html')
