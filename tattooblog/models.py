from django.db import models


# Create your models here.
class TattooPost(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    date = models.DateField(auto_now_add=True)
    authorofpost = models.TextField(blank=True, null=True, max_length=50)
    # image =


def __str__(self):
    return self.title
