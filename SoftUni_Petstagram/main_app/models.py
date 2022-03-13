import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from SoftUni_Petstagram.main_app.validators import alpha_only_validator, validate_max_size

UserModel = get_user_model()  # will get user model from settings AUTH_USER_MODEL = 'accounts_app.PetstagramUser'


class Profile(models.Model):
    MALE_GENDER = ("Male", "Male")
    FEMALE_GENDER = ("Female", "Female")
    DO_NOT_SHOW_GENDER = ("Do not show", "Do not show")
    GENDER_CHOICES = [MALE_GENDER, FEMALE_GENDER, DO_NOT_SHOW_GENDER]

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True)

    first_name = models.CharField(
        max_length=30,
        validators=(MinLengthValidator(2), alpha_only_validator)
    )
    last_name = models.CharField(
        max_length=30,
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


class Pet(models.Model):
    PET_TYPES = [("Cat", "Cat"),
                 ("Dog", "Dog"),
                 ("Bunny", "Bunny"),
                 ("Parrot", "Parrot"),
                 ("Fish", "Fish"),
                 ("Other", "Other"), ]

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=30)
    type = models.CharField(max_length=max([len(x) for (x, _) in PET_TYPES]), choices=PET_TYPES)
    date_of_birth = models.DateField(null=True, blank=True)

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    # All pets' names should be unique for that user
    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return f"{self.name} {self.type}"


class PetPhoto(models.Model):
    photo = models.ImageField(
        upload_to='images',
        # validators=validate_max_size
    )
    tagged_pets = models.ManyToManyField(Pet)
    description = models.TextField(null=True, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
