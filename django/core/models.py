from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower


# Create your models here.

# BikeWorkshop
# User
# Rating


def validator_workshoprepair_name_begins_with_a(value):
    if not value.startswith('a'):
        raise ValidationError('Workshop Repair name must begin with "a"')


class WorkshopRepair(models.Model):
    class TypeWorkshop(models.TextChoices):
        MOTORCYCLE = "MC", "Motorcycle"
        CAR = "CR", "Car"
        BUSTRUCK = "BT", "Bus/Truck"
        OTHER = "OT", "Other"


    name = models.CharField(max_length=100, validators=[validator_workshoprepair_name_begins_with_a])
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField(
        validators=[
            MinValueValidator(-90),
            MaxValueValidator(90)
        ]
    )
    longitude = models.FloatField(
        validators=[
            MinValueValidator(-180),
            MaxValueValidator(180)
        ]
    )
    workshop_type = models.CharField(
        max_length=2,
        choices=TypeWorkshop.choices,
    )
    capacity = models.PositiveSmallIntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = [Lower('name')]
        get_latest_by = 'date_opened'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        print(self._state.adding)
        super().save(*args, **kwargs)


class Staff(models.Model):
    name = models.CharField(max_length=120)
    workshoprepairs = models.ManyToManyField(WorkshopRepair, through='StaffWorkshoprepair')

    def __str__(self):
        return self.name
    
class StaffWorkshoprepair(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    workshoprepair = models.ForeignKey(WorkshopRepair, on_delete=models.CASCADE)
    salary = models.FloatField(null=True)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workshoprepair = models.ForeignKey(WorkshopRepair, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    def __str__(self):
        return f"Rating: {self.rating}"
    

class Sale(models.Model):
    workshoprepair = models.ForeignKey(WorkshopRepair, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=12, decimal_places=2)
    expenditure = models.DecimalField(max_digits=12, decimal_places=2)
    datetime = models.DateTimeField()