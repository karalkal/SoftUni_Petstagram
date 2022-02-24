from django.shortcuts import render, redirect

from SoftUni_Petstagram.main_app.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from SoftUni_Petstagram.main_app.helpers import get_profile
from SoftUni_Petstagram.main_app.models import Profile, PetPhoto, Pet


def profile_details(request):
    profile = get_profile()

    all_photos_for_profile = PetPhoto.objects \
        .filter(tagged_pets__owner=profile) \
        .distinct()

    total_likes_count = sum([pp.likes for pp in all_photos_for_profile])
    photos_count = all_photos_for_profile.count()

    return render(request, 'profile_details.html',
                  {'profile': profile,
                   'total_likes_count': total_likes_count,
                   'photos_count': photos_count,
                   })


def create_profile_view(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()
    return render(request, 'profile_create.html', {'form': form})


def edit_profile_view(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=profile)
    return render(request, 'profile_edit.html', {'form': form})


def delete_profile_view(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()  # save() is overwritten in formssssssssss
            return redirect('home')
    else:
        form = DeleteProfileForm(instance=profile)
    return render(request, 'profile_delete.html', {'form': form})
