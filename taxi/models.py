from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class Car(models.Model):
    model = models.CharField(max_length=50)
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    drivers = models.ManyToManyField("Driver", related_name="cars")

    class Meta:
        constraints = [
            UniqueConstraint(fields=["model", "manufacturer"],
                             name="unique_car"),
        ]

    def __str__(self):
        return f"{self.manufacturer}, {self.model}"


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name})"
