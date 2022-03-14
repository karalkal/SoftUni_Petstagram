import datetime

from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()  # will get user model from settings AUTH_USER_MODEL = 'accounts_app.PetstagramUser'


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
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    photo = models.ImageField(
        upload_to='images',
        # validators=validate_max_size
    )
    tagged_pets = models.ManyToManyField(Pet)
    description = models.TextField(null=True, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
