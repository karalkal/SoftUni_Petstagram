from datetime import datetime

from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from SoftUni_Petstagram.accounts_app.models import Profile, PetstagramUser
from SoftUni_Petstagram.main_app.models import PetPhoto, Pet


class CreateProfileForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(max_length=Profile.F_NAME_MAX_LEN)
    last_name = forms.CharField(max_length=Profile.L_NAME_MAX_LEN)
    profile_picture = forms.URLField()
    date_of_birth = forms.DateField()
    description = forms.CharField(max_length=80, widget=forms.Textarea, )
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=Profile.GENDER_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # To hide/edit help_text
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        # To add class to all form fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            profile_picture=self.cleaned_data['profile_picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            description=self.cleaned_data['description'],
            email=self.cleaned_data['email'],
            gender=self.cleaned_data['gender'],
            user=user
        )
        if commit:
            profile.save()

        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2',
                  # 'first_name', 'last_name', 'profile_picture', 'gender',
                  )
        # exclude - which fields to exclude

        labels = {
            'password1': 'Enter Password',
            'password2': 'Confirm Password',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Link to Profile Picture',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': "Enter first name",
                       }),

            'last_name': forms.TextInput(
                attrs={'placeholder': "Enter last name",
                       }),

            'profile_picture': forms.URLInput(
                attrs={'placeholder': "Enter URL",
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
        related_user_pk = PetstagramUser.object.get(pk=self.instance.pk)
        # owners_pets = self.instance.pet_set.all()
        owners_pets = Pet.objects.filter(user_id=related_user_pk)
        owners_photos = PetPhoto.objects.filter(user_id=related_user_pk)
        owners_photos.delete()  # CASCADE should do that if implemented properly
        owners_pets.delete()
        self.instance.delete()
        PetstagramUser(related_user_pk).delete()
        return self.instance
