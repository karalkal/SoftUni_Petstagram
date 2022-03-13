from django.urls import path

from SoftUni_Petstagram.accounts_app.views import UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login user"),
]
