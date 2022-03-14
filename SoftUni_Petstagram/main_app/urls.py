from django.urls import path
from .views.generic import HomeView, DashboardView, error_401
from .views.profiles import ProfileDetailsView, create_profile_view, edit_profile_view, delete_profile_view
from .views.pet_photos import PetPhotoDetailsView, like_pet_photo, CreatePetPhotoView, edit_pet_photo, delete_pet_photo
from .views.pets import CreatePetView, EditPetView, DeletePetView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('401_error/', error_401, name="401_error"),

    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name="profile"),
    # path('profile/<int:pk>/', profile_details, name="profile"),
    path('profile/create/', create_profile_view, name="create profile"),
    path('profile/edit/', edit_profile_view, name="edit profile"),
    path('profile/delete/', delete_profile_view, name="delete profile"),

    path('photo/details/<int:pk>/', PetPhotoDetailsView.as_view(), name="pet photo details"),
    path('photo/like/<int:pk>/', like_pet_photo, name="like pet photo"),
    path('photo/add/', CreatePetPhotoView.as_view(), name="add pet photo"),
    path('photo/edit/<int:pk>/ ', edit_pet_photo, name="edit pet photo"),
    path('photo/delete/<int:pk>/ ', delete_pet_photo, name="delete pet photo"),

    path('pet/add/', CreatePetView.as_view(), name="add pet"),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name="edit pet"),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name="delete pet"),

]
