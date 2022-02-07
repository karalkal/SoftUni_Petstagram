from django.core.validators import MinLengthValidator
from django.db import models

from SoftUni_Petstagram.main_app.validators import alpha_only_validator, validate_max_size


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

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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

    def __str__(self):
        return f"{self.name} {self.type}"


class PetPhoto(models.Model):
    photo = models.ImageField(
        # validators=validate_max_size
    )
    tagged_pets = models.ManyToManyField(Pet)
    description = models.TextField(null=True, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
