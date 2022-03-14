from django.contrib import admin

from SoftUni_Petstagram.accounts_app.models import Profile
from SoftUni_Petstagram.main_app.models import Pet


# to show pet_set of the Profile in db admin
class PetInlineAdmin(admin.StackedInline):
    model = Pet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    # inlines = (PetInlineAdmin,)
