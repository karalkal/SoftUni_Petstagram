from django.core.exceptions import ValidationError


def alpha_only_validator(value):
    if not value.isalpha():
        raise ValidationError("Only alphabetical chars are permitted. (Sorry, D'Artagnan, R2D2 etc.")


# DOESN'T WORK, FIX IT!
def validate_max_size(img):
    if img.file.size > 5 * 1024 * 1024:
        raise ValidationError("Posmali, Mango!")
