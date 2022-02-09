from django.contrib import admin

# Register your models here.
from SoftUni_Petstagram.main_app.models import Profile, Pet, PetPhoto


# to show pet_set of the Profile in db admin
class PetInlineAdmin(admin.StackedInline):
    model = Pet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    inlines = (PetInlineAdmin,)


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'owner')


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = (
        'photo',
        'publication_date',
        'likes'
    )