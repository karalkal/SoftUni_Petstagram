from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from SoftUni_Petstagram.main_app.forms import CreatePetForm, DeletePetForm, UpdatePetForm


class CreatePetView(CreateView):
    form_class = CreatePetForm
    template_name = 'main_app/pet_create.html'
    success_url = reverse_lazy('dashboard')

    # Only logged-in users can add pet, adding user to CreatePetForm
    # ATTENTION!
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # get the user
        return kwargs

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.prefetch_related('tagged_pets')
        return queryset


class EditPetView(UpdateView):
    form_class = UpdatePetForm
    template_name = 'main_app/pet_edit.html'


class DeletePetView(DeleteView):
    form_class = DeletePetForm
    template_name = 'main_app/pet_delete.html'
