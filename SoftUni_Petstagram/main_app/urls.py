from django.urls import path
from .views.generic import home, dashboard
from .views.profiles import profile_details, create_profile_view, edit_profile_view, delete_profile_view
from .views.pet_photos import photo_details, like_pet_photo, add_pet_photo, edit_pet_photo, delete_pet_photo
from .views.pets import add_pet, edit_pet, delete_pet

urlpatterns = [
    path('', home, name="home"),
    path('dashboard/', dashboard, name="dashboard"),

    path('profile/', profile_details, name="profile"),
    path('profile/create/', create_profile_view, name="create profile"),
    path('profile/edit/', edit_profile_view, name="edit profile"),
    path('profile/delete/', delete_profile_view, name="delete profile"),

    path('photo/details/<int:pk>/', photo_details, name="pet photo details"),
    path('photo/like/<int:pk>/', like_pet_photo, name="like pet photo"),
    path('photo/add/', add_pet_photo, name="add pet photo"),
    path('photo/edit/<int:pk>/ ', edit_pet_photo, name="edit pet photo"),
    path('photo/delete/<int:pk>/ ', delete_pet_photo, name="delete pet photo"),

    path('pet/add/', add_pet, name="add pet"),
    path('pet/edit/<int:pk>/', edit_pet, name="edit pet"),
    path('pet/delete/<int:pk>/', delete_pet, name="delete pet"),

]
