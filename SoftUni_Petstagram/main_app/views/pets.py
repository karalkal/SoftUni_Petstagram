from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from SoftUni_Petstagram.main_app.forms import CreatePetForm, DeletePetForm, UpdatePetForm


class CreatePetView(CreateView):
    template_name = 'main_app/pet_create.html'
    form_class = CreatePetForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPetView(UpdateView):
    form_class = UpdatePetForm
    template_name = 'main_app/pet_edit.html'


class DeletePetView(DeleteView):
    form_class = DeletePetForm
    template_name = 'main_app/pet_delete.html'
