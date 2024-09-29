from django.db import models

# Create your models here.
class Article(models.Model):
    tittle = models.CharField(max_length=250)
    fill = models.TextField(null=True)
    OPTION_CATEGORY = [
        ('python','python'),
        ('django','django'),
        ('javascript','javascript'),
    ]
    categories = models.CharField(max_length=50, choices=OPTION_CATEGORY)

    def __str__(self):
        return self.tittle