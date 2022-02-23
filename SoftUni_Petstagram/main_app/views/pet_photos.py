from django.shortcuts import render, redirect

from SoftUni_Petstagram.main_app.helpers import get_profile
from SoftUni_Petstagram.main_app.models import PetPhoto


def photo_details(request, pk):
    searched_photo = PetPhoto.objects.prefetch_related('tagged_pets').get(pk=pk)
    context = {"searched_photo": searched_photo}
    return render(request, 'photo_details.html', context)


def like_pet_photo(request, pk):
    liked_photo = PetPhoto.objects.get(pk=pk)
    liked_photo.likes += 1
    liked_photo.save()

    return redirect('pet photo details', pk)


def add_pet_photo(request):
    return render(request, 'photo_create.html')


def edit_pet_photo(request):
    return render(request, 'photo_edit.html')
