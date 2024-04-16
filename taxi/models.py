from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self) -> models.CharField:
        return self.name

    class Meta:
        ordering = ("name",)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("first_name", "last_name",)

    def __str__(self) -> str:
        return f"{self.username}: {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("taxi:driver-detail", args=[str(self.id)])


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(Driver, related_name="cars")

    def __str__(self) -> models.CharField:
        return self.model

    class Meta:
        ordering = ("model",)

    def get_absolute_url(self):
        return reverse("taxi:car-detail", args=[str(self.pk)])
