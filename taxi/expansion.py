from django.core.exceptions import ValidationError


def license_validation(func):
    def inner(*args):
        license_number = func(args[0])
        letter = license_number[:3]
        number = license_number[3:]
        if len(license_number) > 8:
            raise ValidationError("License number must contain exactly 8 characters")
        if not letter.isupper() or not letter.isalpha():
            raise ValidationError("First 3 characters are uppercase letters")
        if not number.isdigit():
            raise ValidationError("Last 5 characters are digits")
        return license_number
    return inner
