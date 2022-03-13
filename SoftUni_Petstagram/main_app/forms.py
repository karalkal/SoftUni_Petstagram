from datetime import datetime

from django import forms

from SoftUni_Petstagram.main_app.helpers import get_profile
from SoftUni_Petstagram.main_app.models import Profile, Pet, PetPhoto


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'profile_picture')
        # exclude - which fields to exclude
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Link to Profile Picture',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': "form-control",
                       'placeholder': "Enter first name",
                       }),

            'last_name': forms.TextInput(
                attrs={'class': "form-control",
                       'placeholder': "Enter last name",
                       }),

            'profile_picture': forms.URLInput(
                attrs={'class': "form-control",
                       'placeholder': "Enter URL",
                       }),
        }


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        self.initial['gender'] = Profile.DO_NOT_SHOW_GENDER

    class Meta:
        model = Profile
        fields = '__all__'
        # exclude - which fields to exclude
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Link to Profile Picture',
            'date_of_birth': 'Date of Birth',
            'email': 'Email',
            'gender': 'Gender',
            'description': 'Description'
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': "form-control",
                       'placeholder': "Enter first name",
                       }),

            'last_name': forms.TextInput(
                attrs={'class': "form-control",
                       'placeholder': "Enter last name",
                       }),

            'profile_picture': forms.TextInput(
                attrs={'class': "form-control",
                       'placeholder': "Enter URL",
                       }),

            'date_of_birth': forms.SelectDateWidget(
                years=range(datetime.now().year, 1920, -1),
                attrs={'class': "form-control",
                       'placeholder': "Enter Date of Birth",
                       # 'min': '1920-01-01',  # doesn't work
                       # 'max': date.today(),  # doesn't work
                       }),

            'email': forms.EmailInput(
                attrs={'class': "form-control",
                       'placeholder': "Enter Email",
                       }),

            'gender': forms.Select(
                choices=Profile.GENDER_CHOICES,
                attrs={'class': "form-control",
                       }
            ),

            'description': forms.Textarea(
                attrs={'class': "form-control",
                       'placeholder': "Enter Description",
                       'rows': 3,
                       }),

        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()  # no fields will be shown

    def save(self, commit=True):
        # owners_pets = Pet.objects.filter(petphoto__tagged_pets__owner=self.instance)
        owners_pets = self.instance.pet_set.all()
        owners_photos = PetPhoto.objects.filter(tagged_pets__user=self.instance)
        owners_photos.delete()
        owners_pets.delete()
        self.instance.delete()  # to remove record from DB
        return self.instance


# ATTENTION! WTF is going on here?!
class CreatePetForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(CreatePetForm, self).__init__(*args, **kwargs)
        self.user = user  # added user to instance of form, will be added below

    def save(self, commit=True):
        # instantiate pet from parent class, but not saving it yet
        pet = super(CreatePetForm, self).save(commit=False)
        pet.user = self.user
        if commit:
            pet.save()

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={'class': "form-control",
                       'placeholder': "Enter Pet Name", }
            ),

            'type': forms.Select(
                choices=Pet.PET_TYPES,
                attrs={'class': "form-control", }
            ),

            'date_of_birth': forms.SelectDateWidget(
                years=range(datetime.now().year, 1920, -1),
                attrs={'class': "form-control", }
            ),
        }


class UpdatePetForm(CreatePetForm):
    pass


class DeletePetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['class'] = "form-control"

    def save(self, commit=True):
        self.instance.delete()  # to remove record from DB
        return self.instance

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')


class AddPetPhotoForm(forms.ModelForm):
    # pass
    class Meta:
        owners_pets = Pet.objects.filter(user=get_profile())

        PET_TYPES = [(x.type, x.type) for x in owners_pets]  # ("Cat", "Cat"), ("Dog", "Dog"),
        model = PetPhoto
        fields = ('photo', 'description', 'tagged_pets')
        labels = {'photo': "Pet Image",
                  'tagged_pets': "Tag Pets"}
        widgets = \
            {
                'photo': forms.FileInput(
                    attrs={'class': "form-control-file", }
                ),

                'description': forms.Textarea(
                    attrs={'rows': 3,
                           'class': "form-control",
                           'placeholder': "Enter Description",
                           }
                ),

                'tagged_pets': forms.SelectMultiple(
                    choices=PET_TYPES,  # Shows only names of all created pets in the profile.
                    attrs={'class': "form-control",
                           'required': True,
                           }
                )
            }


class EditPetPhotoForm(forms.ModelForm):
    # pass
    class Meta:
        owners_pets = Pet.objects.filter(user=get_profile())
        PET_TYPES = [(x.type, x.type) for x in owners_pets]  # ("Cat", "Cat"), ("Dog", "Dog"),
        model = PetPhoto
        fields = ('description', 'tagged_pets')
        labels = {'photo': "Pet Image",
                  'tagged_pets': "Tag Pets"}
        widgets = {
            # 'photo': forms.FileInput(
            #     attrs={'class': "form-control-file",
            #            'disabled': True, 'hidden': True}
            # ),

            'description': forms.Textarea(
                attrs={'rows': 3,
                       'class': "form-control",
                       }
            ),

            'tagged_pets': forms.SelectMultiple(
                choices=PET_TYPES,  # Shows only names of all created pets in the profile.
                attrs={'class': "form-control",
                       'required': True,
                       }
            )
        }
