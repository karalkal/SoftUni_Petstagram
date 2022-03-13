from django.contrib.auth import models as auth_models
from django.db import models

from SoftUni_Petstagram.accounts_app.managers import PetstagramUserManager

'''
1. Create model extending...                see imports and model below
2. Configure this model in settings.py      i.e. AUTH_USER_MODEL = 'accounts_app.PetstagramUser'
3. Create user manager
'''


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LEN = 35
    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'  # see    def get_username(self):    in AbstractBaseUser

    object = PetstagramUserManager()
