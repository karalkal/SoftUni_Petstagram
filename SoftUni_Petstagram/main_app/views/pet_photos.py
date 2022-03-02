from django.shortcuts import render, redirect

from SoftUni_Petstagram.main_app.forms import AddPetPhotoForm, EditPetPhotoForm
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
    if request.method == 'POST':
        form = AddPetPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AddPetPhotoForm()

    return render(request, 'photo_create.html', {'form': form})


def edit_pet_photo(request, pk):
    photo_to_edit = PetPhoto.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditPetPhotoForm(request.POST, request.FILES, instance=photo_to_edit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditPetPhotoForm(instance=photo_to_edit)

    return render(request, 'photo_edit.html',
                  {'form': form,
                   'photo_to_edit': photo_to_edit})


def delete_pet_photo(request, pk):
    PetPhoto.objects.get(pk=pk).delete()
    return redirect('dashboard')
