from django.db import models


class KontakModel(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)