from django.shortcuts import render, redirect
from django.views.generic import DetailView

from SoftUni_Petstagram.main_app.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from SoftUni_Petstagram.main_app.helpers import get_profile
from SoftUni_Petstagram.main_app.models import Profile, PetPhoto, Pet


# def profile_details(request, pk):
#     profile = Profile.objects.get(pk=pk)
#     pets_for_profile = list(Pet.objects.filter(user_id=profile.user_id))  # self.object is a profile
#
#     # to get number of likes and number of photos per profile
#     pet_photos = PetPhoto.objects \
#         .filter(tagged_pets__in=pets_for_profile) \
#         .distinct()
#     total_likes_count = sum([pp.likes for pp in pet_photos])
#     photos_count = pet_photos.count()
#     context = {
#         'profile': profile,
#         'total_likes_count': total_likes_count,
#         'photos_count': photos_count,
#         'pets_for_profile': pets_for_profile,
#     }
#     return render(request, 'main_app/profile_details.html', context)


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'main_app/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets_for_profile = list(Pet.objects.filter(user_id=self.object.user_id))  # self.object is a profile

        # to get number of likes and number of photos per profile
        pet_photos = PetPhoto.objects \
            .filter(tagged_pets__in=pets_for_profile) \
            .distinct()
        total_likes_count = sum([pp.likes for pp in pet_photos])
        photos_count = pet_photos.count()

        context.update(  # will merge both dicts, i.e. this to the empty one
            {'pets_for_profile': pets_for_profile,
             'total_likes_count': total_likes_count,
             'photos_count': photos_count,
             }
        )
        return context


def create_profile_view(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()
    return render(request, 'main_app/profile_create.html', {'form': form})


def edit_profile_view(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=profile)
    return render(request, 'main_app/profile_edit.html', {'form': form})


def delete_profile_view(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()  # save() is overwritten in forms
            return redirect('home')
    else:
        form = DeleteProfileForm(instance=profile)
    return render(request, 'main_app/profile_delete.html', {'form': form})
