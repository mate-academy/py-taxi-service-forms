from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"

    def __str__(self):
        return f"{self.name} ({self.country})"

    def get_absolute_url(self):
        return reverse("taxi:manufacturer-list")


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("taxi:driver-detail", kwargs={"pk": self.pk})


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.PROTECT,
        related_name="manufactured_cars"
    )
    year = models.PositiveIntegerField(default=2020)
    capacity = models.PositiveIntegerField(default=4)
    drivers = models.ManyToManyField(Driver, related_name="cars")

    class Meta:
        ordering = ["model"]
        verbose_name = "car"
        verbose_name_plural = "cars"

    def __str__(self):
        return f"{self.model} ({self.year}) - {self.manufacturer.name}"

    def get_absolute_url(self):
        return reverse("taxi:car-detail", kwargs={"pk": self.pk})
