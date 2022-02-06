from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.main_app.validators import alpha_only_validator


class Profile(models.Model):
    GENDER_CHOICES = [("Male", "Male"), ("Female", "Female"), ("Do not show", "Do not show")]
    first_name = models.CharField(max_length=30,
                                  validators=(MinLengthValidator(2), alpha_only_validator))
    last_name = models.CharField(max_length=30,
                                 validators=(MinLengthValidator(2), alpha_only_validator))
    profile_picture = models.URLField()
    # The user may provide the following information in their profile:
    date_of_birth = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=max([len(x) for (x, _) in GENDER_CHOICES]),
                              null=True, blank=True, choices=GENDER_CHOICES)


class Pet(models.Model):
    PET_TYPES = [
        ("Cat", "Cat"),
        ("Dog", "Dog"),
        ("Bunny", "Bunny"),
        ("Parrot", "Parrot"),
        ("Fish", "Fish"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=30)
    type = models.CharField(max_length=max([len(x) for (x, _) in PET_TYPES]), choices=PET_TYPES)
    dob = models.DateTimeField(null=True, blank=True)

    # foreign key
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # All pets' names should be unique for that user
    class Meta:
        unique_together = ('owner', 'name')

