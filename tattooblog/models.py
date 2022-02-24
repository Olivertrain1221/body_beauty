from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class TattooPost(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    date = models.DateField(auto_now_add=True)
    body = models.TextField(blank=True, null=True, max_length=50)
    image = CloudinaryField('image', default="https://res.cloudinary.com/dxsodecl1/image/upload/v1644248279/cld-sample.jpg")
    #username added

def __str__(self):
    return self.title


def info(self):
    return self.body[:20]
