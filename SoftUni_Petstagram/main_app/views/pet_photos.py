from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from SoftUni_Petstagram.main_app.forms import AddPetPhotoForm, EditPetPhotoForm
from SoftUni_Petstagram.main_app.models import PetPhoto, Pet


class PhotoDetailsView(LoginRequiredMixin, DetailView):
    model = PetPhoto
    template_name = 'main_app/photo_details.html'
    context_object_name = 'searched_photo'


def like_pet_photo(request, pk):
    liked_photo = PetPhoto.objects.get(pk=pk)
    liked_photo.likes += 1
    liked_photo.save()

    return redirect('pet photo details', pk)


# TODO Shouldn't be able to add pet photo if no pets are created
class CreatePetPhotoView(LoginRequiredMixin, CreateView):
    model = PetPhoto
    template_name = 'main_app/photo_create.html'
    fields = ('photo', 'description', 'tagged_pets')
    success_url = reverse_lazy('dashboard')


def edit_pet_photo(request, pk):
    photo_to_edit = PetPhoto.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditPetPhotoForm(request.POST, request.FILES, instance=photo_to_edit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditPetPhotoForm(instance=photo_to_edit)

    return render(request, 'main_app/photo_edit.html',
                  {'form': form,
                   'photo_to_edit': photo_to_edit})


def delete_pet_photo(request, pk):
    photo_to_delete = PetPhoto.objects.get(pk=pk)
    photo_to_delete.delete()
    return redirect('dashboard')
