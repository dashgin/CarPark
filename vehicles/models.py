from django.db import models

from drivers.models import Driver
from helpers.models import TimeStampedModel

from .validators import plate_number_validator


class Vehicle(TimeStampedModel):
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=50, unique=True, validators=[plate_number_validator])
