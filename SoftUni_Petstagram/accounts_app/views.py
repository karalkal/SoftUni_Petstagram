from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from SoftUni_Petstagram.accounts_app.forms import CreateProfileForm, DeleteProfileForm, EditProfileForm
from SoftUni_Petstagram.accounts_app.models import Profile
from SoftUni_Petstagram.common.view_mixins import RedirectToDashboard
from SoftUni_Petstagram.main_app.models import PetPhoto, Pet


class UserRegisterView(RedirectToDashboard, CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts_app/profile_create.html'
    success_url = reverse_lazy('login user')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts_app/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    template_name = 'accounts_app/logout_page.html'
    success_url = reverse_lazy('home')


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    success_url = reverse_lazy('dashboard')


'''
Profile Views (moved from main_app)
'''


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
    template_name = 'accounts_app/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets_for_profile = list(Pet.objects.filter(user_id=self.object.user_id))  # self.object is a profile
        # pets_for_profile = self.request.user.pet_set # Trying 2nd option - not working

        # to get number of likes and number of photos per profile
        # TODO This only returns photos for pets owned by the logged in user but they could tag pets they don't own
        pet_photos = PetPhoto.objects \
            .filter(tagged_pets__in=pets_for_profile) \
            .distinct()
        total_likes_count = sum([pp.likes for pp in pet_photos])
        photos_count = pet_photos.count()

        is_owner_of_profile = False
        if self.object.user_id == self.request.user.id:
            is_owner_of_profile = True

        context.update(  # will merge both dicts, i.e. this to the empty one
            {'pets_for_profile': pets_for_profile,
             'total_likes_count': total_likes_count,
             'photos_count': photos_count,
             'is_owner_of_profile': is_owner_of_profile,
             }
        )
        return context


# def create_profile_view(request):
#     if request.method == 'POST':
#         form = CreateProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = CreateProfileForm()
#     return render(request, 'main_app/profile_create.html', {'form': form})


# class EditProfileView():
#     pass

def edit_profile_view(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', profile.pk)
    else:
        form = EditProfileForm(instance=profile)
    return render(request, 'accounts_app/profile_edit.html',
                  {'form': form,
                   'profile': profile, })


def delete_profile_view(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()  # save() is overwritten in forms
            return redirect('home')
    else:
        form = DeleteProfileForm(instance=profile)
    return render(request, 'accounts_app/profile_delete.html',
                  {'form': form,
                   'profile': profile, })
