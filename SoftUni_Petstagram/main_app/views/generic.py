from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from SoftUni_Petstagram.main_app.models import Profile, PetPhoto, Pet


class HomeView(TemplateView):
    template_name = 'main_app/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_menu_items'] = True  # add this to context dict
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class DashboardView(ListView):
    model = PetPhoto
    template_name = 'main_app/dashboard.html'
    context_object_name = 'pet_photos'


def error_401(request):
    return render(request, 'main_app/401_error.html')
