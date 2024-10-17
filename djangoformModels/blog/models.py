from django.db import models
from django.core import validators
from .validation import *


# Create your models here.
class Article(models.Model):
    title = models.CharField(
        max_length=100,
        validators=[validators.MaxLengthValidator(5)]
    )
    article = models.TextField(
        validators=[validate_article]
    )
    CATEGORIES = (
        ('blog','blog'),
        ('berita','berita'),
        ('viral','viral'),
    )
    category = models.CharField(
        max_length=50, 
        choices=CATEGORIES,
        default='blog',
    )
    dateTime = models.DateTimeField(auto_now_add=True)
    writer = models.CharField(
        max_length=50, 
        validators=[validate_writer]
    )

    def __str__(self):
        return "{} {}".format(self.id, self.title)

