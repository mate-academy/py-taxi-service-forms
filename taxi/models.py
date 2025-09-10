from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.license_number}"

    def get_absolute_url(self):
        return reverse("taxi:driver-detail", kwargs={"pk": self.pk})


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )
    model = models.CharField(max_length=255)

    class Meta:
        ordering = ("manufacturer", "model")

    def __str__(self):
        return (f"{self.manufacturer.name} "
                f"{self.manufacturer.country}: "
                f"{self.model}")

    def get_absolute_url(self):
        return reverse("taxi:car-detail", kwargs={"pk":self.pk})


class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    birth_year = models.IntegerField()
    hobby = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural= "customers"

    def __set__(self):
        return self.full_name
