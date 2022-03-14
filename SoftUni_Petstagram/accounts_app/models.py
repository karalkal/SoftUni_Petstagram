from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from SoftUni_Petstagram.accounts_app.managers import PetstagramUserManager
from SoftUni_Petstagram.common.validators import alpha_only_validator

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


class Profile(models.Model):
    MALE_GENDER = ("Male", "Male")
    FEMALE_GENDER = ("Female", "Female")
    DO_NOT_SHOW_GENDER = ("Do not show", "Do not show")
    GENDER_CHOICES = [MALE_GENDER, FEMALE_GENDER, DO_NOT_SHOW_GENDER]
    F_NAME_MAX_LEN = 30
    L_NAME_MAX_LEN = 30

    user = models.OneToOneField(
        PetstagramUser,  # Can import and use UserModel as well
        on_delete=models.CASCADE,
        primary_key=True)

    first_name = models.CharField(
        max_length=F_NAME_MAX_LEN,
        validators=(MinLengthValidator(2), alpha_only_validator)
    )
    last_name = models.CharField(
        max_length=L_NAME_MAX_LEN,
        validators=(MinLengthValidator(2), alpha_only_validator)
    )
    profile_picture = models.URLField()

    # The user MAY provide the following information in their profile:
    date_of_birth = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(
        max_length=max([len(x) for (x, _) in GENDER_CHOICES]),
        null=True, blank=True,
        choices=GENDER_CHOICES,
        default=DO_NOT_SHOW_GENDER[1],
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
