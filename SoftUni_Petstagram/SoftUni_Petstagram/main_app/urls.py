from django.urls import path
from .views import home, dashboard, profile, photo_details
# from . import views
# if you want to use view.dashboard etc

urlpatterns = [
    path('', home, name="home"),
    path('dashboard/', dashboard, name="dashboard"),
    path('profile/', profile, name="profile"),
    path('photo/details/<int:pk>/', photo_details, name="pet_photo_details"),
]
