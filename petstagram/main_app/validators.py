from django.core.exceptions import ValidationError


def alpha_only_validator(value):
    if not value.is_alpha():
        raise ValidationError("Only alphabetical chars are permitted. (Sorry, D'Artagnan, R2D2 etc.")
