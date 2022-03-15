from django.urls import path
from django.views.generic import RedirectView

from SoftUni_Petstagram.accounts_app.views import UserLoginView, UserLogoutView, ProfileDetailsView, UserRegisterView, \
    ChangeUserPasswordView, edit_profile_view, delete_profile_view

urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login user"),
    path('logout/', UserLogoutView.as_view(), name="logout user"),

    path('details/<int:pk>/', ProfileDetailsView.as_view(), name="profile"),
    path('create/', UserRegisterView.as_view(), name="create profile"),
    path('change_password/', ChangeUserPasswordView.as_view(), name="change password"),
    path('profile/edit/<int:pk>', edit_profile_view, name="edit profile"),
    path('profile/delete/<int:pk>', delete_profile_view, name="delete profile"),
]
