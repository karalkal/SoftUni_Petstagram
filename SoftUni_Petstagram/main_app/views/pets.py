from django.shortcuts import render, redirect

from SoftUni_Petstagram.main_app.forms import CreatePetForm, DeletePetForm
from SoftUni_Petstagram.main_app.helpers import get_profile
from SoftUni_Petstagram.main_app.models import Pet, PetPhoto

from django.db import IntegrityError


def add_pet(request):
    instance = Pet(owner=get_profile())

    #  if redirected here from add_pet_photo(request) with no pets to tag to the photo
    #  something like - 'pets_found': pets_found

    if request.method == 'POST':
        form = CreatePetForm(request.POST, instance=instance)
        # Check if unique_together is satisfied, if not display relevant message in template
        # There must be a simpler, better solution...
        if form.is_valid():
            try:
                form.save()
            except IntegrityError as error:
                # print(error)
                return render(request, 'pet_create.html',
                              {'form': form,
                               'error': error,
                               })

            return redirect('profile')
    else:  # if GET
        form = CreatePetForm(instance=instance)
    return render(request, 'pet_create.html', {'form': form})


def edit_pet(request, pk):
    instance = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreatePetForm(request.POST, instance=instance)
        # Check if unique_together is satisfied, if not display relevant message in template
        # There must be a simpler, better solution...
        if form.is_valid():

            try:
                form.save()
            except IntegrityError as error:
                # print(error)
                return render(request, 'pet_create.html',
                              {'form': form,
                               'error': error})

            return redirect('profile')
    else:
        form = CreatePetForm(instance=instance)
    return render(request, 'pet_edit.html', {'form': form,
                                             'instance': instance})


def delete_pet(request, pk):
    instance = Pet.objects.get(pk=pk)
    # To delete photo if this pet is the only one tagged to it
    # 1. get all photos where this pet is tagged
    photos_with_this_pet = instance.petphoto_set.all()
    if request.method == 'POST':
        form = DeletePetForm(request.POST, instance=instance)
        for photo in photos_with_this_pet:

            # 2. check if it is the only one and if yes, delete it
            if photo.tagged_pets.count() <= 1:
                photo.delete()
        form.save()  # save method is overwritten in form

        return redirect('profile')
    else:
        form = DeletePetForm(instance=instance)
    return render(request, 'pet_delete.html', {'form': form,
                                               'instance': instance})
