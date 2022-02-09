from django.urls import path
from .views import home, dashboard, profile, photo_details, like_pet_photo

# from . import views
# if you want to use view.dashboard etc

urlpatterns = [
    path('', home, name="home"),
    path('dashboard/', dashboard, name="dashboard"),
    path('profile/', profile, name="profile"),
    path('photo/details/<int:pk>/', photo_details, name="pet photo details"),
    path('photo/like/<int:pk>/', like_pet_photo, name="like pet photo"),
]
