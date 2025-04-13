from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.utils import timezone


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


    name = models.CharField(
        max_length=100, 
        validators=[validator_workshoprepair_name_begins_with_a],
    )
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
    nickname = models.CharField(max_length=200, default='')
    comments = GenericRelation("Comment", related_query_name='workshoprepair')

    @property
    def workshoprepair__name(self):
        return self.nickname or self.name

    @property
    def was_opened_this_year(self) -> bool:
        current_year = timezone.now().year
        return self.date_opened.year == current_year
    
    def is_opened_after(self, date: date) -> bool:
        return self.date_opened > date

    class Meta:
        ordering = [Lower('name')]
        get_latest_by = 'date_opened'
        constraints = [
            models.CheckConstraint(
                name="validated_latitude",
                check=Q(latitude__gte=-90, latitude__lte=90),
                violation_error_message="Invalid Latitude"
            ),
            models.CheckConstraint(
                name="validated_longitude",
                check=Q(longitude__gte=-180, longitude__lte=180),
                violation_error_message="Invalid Longitude"
            ),
            models.UniqueConstraint(
                Lower('name'),
                name="name_uniq_constraint",
            )
        ]

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
    comments = GenericRelation("Comment")


    def __str__(self):
        return f"Rating: {self.rating}"
    

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='rating_value_validate',
                check=Q(rating__gte=1, rating__lte=5),
                violation_error_message="Rating Invalid: Must Fall Between 1 And 5."
            ),
            models.UniqueConstraint(
                fields=['user', 'workshoprepair'],  
                name='user_workshop_uniq',
            )
        ]
    

class Sale(models.Model):
    workshoprepair = models.ForeignKey(WorkshopRepair, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=12, decimal_places=2)
    expenditure = models.DecimalField(max_digits=12, decimal_places=2)
    datetime = models.DateTimeField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    number_in_stock = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_of_items = models.PositiveSmallIntegerField()
    # user

    def __str__(self):
        return f"{self.number_of_items} x {self.product.name}"
    

class Comment(models.Model):
    text = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveSmallIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')