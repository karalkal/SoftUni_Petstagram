from django.contrib import admin

# Register your models here.
from SoftUni_Petstagram.main_app.models import Pet, PetPhoto


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'user')


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    @staticmethod
    def tagged(obj):
        return ", ".join([p.name for p in obj.tagged_pets.all()])

    list_display = (
        'tagged',
        'publication_date',
        'likes',
        'photo'
    )
