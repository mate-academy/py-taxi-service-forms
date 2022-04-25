from django.core.exceptions import ValidationError

DRIVER_LICENSE_NUMBER_LETTERS_IN_UPPER = 3
DRIVER_LICENSE_NUMBER_MAX_LENGHT = 8
DRIVER_LICENSE_NUMBER_NUMBER_OF_NUM_LETTERS = 5


def license_number_validator(value):
    if not value[:DRIVER_LICENSE_NUMBER_LETTERS_IN_UPPER].isupper():
        raise ValidationError(
            f"First {DRIVER_LICENSE_NUMBER_LETTERS_IN_UPPER}"
            f" letters must be in uppercase"
        )
    if not len(value) == DRIVER_LICENSE_NUMBER_MAX_LENGHT:
        raise ValidationError(f"License number must contain "
                              f"{DRIVER_LICENSE_NUMBER_MAX_LENGHT} letters")
    if not value[-DRIVER_LICENSE_NUMBER_NUMBER_OF_NUM_LETTERS:].isnumeric():
        raise ValidationError(
            f"Last letters {DRIVER_LICENSE_NUMBER_NUMBER_OF_NUM_LETTERS}"
            f" must be digits"
        )
