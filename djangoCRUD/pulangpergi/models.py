from django.db import models
from django.utils.text import slugify


# Create your models here.
class Destination(models.Model):
    nameCustomer = models.CharField(max_length=50)
    nameDriver = models.CharField(max_length=50)
    destination = models.TextField()
    profile = models.ImageField(blank=True, default='profile.png')
    slug = models.SlugField(blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nameCustomer)
        super(Destination, self).save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.id, self.nameCustomer)