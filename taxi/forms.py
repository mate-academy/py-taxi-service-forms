from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from taxi.models import Driver


class DriverCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ("license_number",
                                                 "first_name",
                                                 "last_name")

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) == 8 \
                and license_number[:3].isupper() \
                and license_number[-5:].isdigit():
            return license_number
        else:
            raise ValidationError("Number should have 3 uppercase letters "
                                  "and 5 digits - ABC:12345")
