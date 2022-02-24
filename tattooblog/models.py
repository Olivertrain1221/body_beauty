from django.db import models


# Create your models here.
class TattooPost(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    date = models.DateField(auto_now_add=True)
    # image =


def __str__(self):
    return self.title
