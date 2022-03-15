from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from SoftUni_Petstagram.main_app.forms import CreatePetForm, UpdatePetForm
from SoftUni_Petstagram.main_app.models import Pet


class CreatePetView(CreateView):
    form_class = CreatePetForm
    template_name = 'main_app/pet_create.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPetView(UpdateView):
    model = Pet
    form_class = UpdatePetForm
    template_name = 'main_app/pet_edit.html'

    # success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        # capture that 'pk' as profile_id and pass it to 'reverse_lazy()' function
        profile_id = self.object.user.pk
        return reverse_lazy('profile', kwargs={'pk': profile_id})

    # adds user after form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class DeletePetView(DeleteView):
    model = Pet
    template_name = 'main_app/pet_delete.html'

    def get_context_data(self, **kwargs):
        return super(DeletePetView, self).get_context_data(**kwargs)

    def get_success_url(self):
        # capture that 'pk' as profile_id and pass it to 'reverse_lazy()' function
        profile_id = self.object.user.pk
        return reverse_lazy('profile', kwargs={'pk': profile_id})
