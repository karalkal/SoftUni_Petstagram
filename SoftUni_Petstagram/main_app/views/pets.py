from django.shortcuts import render, redirect

from SoftUni_Petstagram.main_app.forms import CreatePetForm
from SoftUni_Petstagram.main_app.helpers import get_profile
from SoftUni_Petstagram.main_app.models import Pet

from django.db import IntegrityError


def add_pet(request):
    instance = Pet(owner=get_profile())
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
    return render(request, 'pet_create.html', {'form': form})


def edit_pet(request, pk):
    return render(request, 'pet_edit.html')


def delete_pet(request, pk):
    return render(request, 'pet_delete.html')
