from django.shortcuts import render, redirect

from SoftUni_Petstagram.main_app.helpers import get_profile
from SoftUni_Petstagram.main_app.models import Profile, PetPhoto, Pet


def home(request):
    context = {'hide_additional_menu_items': True}
    return render(request, 'home_page.html', context)


def dashboard(request):
    # check pets for specific user, in our case first one
    profile = get_profile()
    if not profile:
        return redirect('401_error.html')

    # owners_pets = profile.pet_set.all()
    owners_pets_photos = set(PetPhoto.objects
                             .prefetch_related('tagged_pets')
                             .filter(tagged_pets__owner=profile))

    context = {"owners_pets_photos": owners_pets_photos}
    return render(request, 'dashboard.html', context)
