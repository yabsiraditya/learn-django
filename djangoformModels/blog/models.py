from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    article = models.TextField()
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
    writer = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.id, self.title)

