from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=255,
        unique=True
    )

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.license_number})"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        Driver,
        related_name="cars"
    )

    class Meta:
        ordering = ["model"]

    def __str__(self):
        return self.model
