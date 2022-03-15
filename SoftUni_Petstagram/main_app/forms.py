from datetime import datetime
from django import forms
from SoftUni_Petstagram.main_app.models import Pet, PetPhoto


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

        return pet  # DON'T FORGET

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


class UpdatePetForm(CreatePetForm, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)  # Displays error without user in args
        self.user = user

    def save(self, commit=True):
        pet = super().save(commit=False)
        pet.user = self.user
        if commit:
            pet.save()
        return pet  # DON'T FORGET

    # class Meta inherited from CreatePetForm


'''
class DeletePetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            # field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['class'] = "form-control"

    def save(self, commit=True):
        self.instance.delete()  # to remove record from DB
        return self.instance

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
'''


class AddPetPhotoForm(forms.ModelForm):
    # pass
    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'tagged_pets')
        labels = {'photo': "Pet Image",
                  'tagged_pets': "Tag Pets"}
        widgets = {
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
                # choices=PET_TYPES,  # Shows only names of all created pets in the profile. ** NOT ANYMORE
                choices=Pet.PET_TYPES,
                attrs={'class': "form-control",
                       'required': True,
                       }
            )
        }


class EditPetPhotoForm(forms.ModelForm):
    # pass
    class Meta:
        model = PetPhoto
        fields = ('description', 'tagged_pets')
        labels = {'photo': "Pet Image",
                  'tagged_pets': "Tag Pets"}
        widgets = {
            'description': forms.Textarea(
                attrs={'rows': 3,
                       'class': "form-control",
                       }
            ),
            'tagged_pets': forms.SelectMultiple(
                choices=Pet.PET_TYPES,
                attrs={'class': "form-control",
                       'required': True,
                       }
            )
        }
