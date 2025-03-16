from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# BikeWorkshop
# User
# Rating

class WorkshopRepair(models.Model):
    class TypeWorkshop(models.TextChoices):
        MOTORCYCLE = "MC", "Motorcycle"
        CAR = "CR", "Car"
        BUSTRUCK = "BT", "Bus/Truck"
        OTHER = "OT", "Other"


    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    workshop_type = models.CharField(
        max_length=2,
        choices=TypeWorkshop.choices,
    )

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workshoprepair = models.ForeignKey(WorkshopRepair, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Rating: {self.rating}"
    

class Sale(models.Model):
    workshoprepair = models.ForeignKey(WorkshopRepair, on_delete=models.SET_NULL, null=True)
    income = models.DecimalField(max_digits=12, decimal_places=2)
    datetime = models.DateTimeField()