from django.urls import path

from SoftUni_Petstagram.accounts_app.views import UserLoginView, ProfileDetailsView, UserRegisterView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login user"),

    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name="profile"),
    # path('profile/<int:pk>/', profile_details, name="profile"),
    path('profile/create/', UserRegisterView.as_view(), name="create profile"),
    # path('profile/create/', create_profile_view, name="create profile"),
    # path('profile/edit/', edit_profile_view, name="edit profile"),
    # path('profile/delete/', delete_profile_view, name="delete profile"),
]
