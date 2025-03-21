from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("taxi:manufacturer-detail", args=[self.id])

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name} {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse("taxi:driver-detail", args=[self.id])


class Car(models.Model):
    model = models.CharField(max_length=55)
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    def get_absolute_url(self):
        return reverse("taxi:car-detail", args=[self.id])

    def __str__(self) -> any:
        return self.model
