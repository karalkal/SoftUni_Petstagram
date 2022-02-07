from django.contrib import admin

# Register your models here.
from SoftUni_Petstagram.main_app.models import Profile, Pet, PetPhoto


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'owner')


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = (
        # 'tagged_pets',
        'publication_date',
        'likes'
    )
