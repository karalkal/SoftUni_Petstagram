# Generated by Django 4.0.3 on 2022-03-14 20:55

import SoftUni_Petstagram.common.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0002_alter_petstagramuser_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), SoftUni_Petstagram.common.validators.alpha_only_validator])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), SoftUni_Petstagram.common.validators.alpha_only_validator])),
                ('profile_picture', models.URLField()),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], default='Do not show', max_length=11, null=True)),
            ],
        ),
    ]
