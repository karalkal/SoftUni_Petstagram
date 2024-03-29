# Generated by Django 4.0.3 on 2022-03-13 05:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_alter_pet_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='owner',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together={('user', 'name')},
        ),
    ]
