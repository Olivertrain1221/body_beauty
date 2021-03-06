from django.db import models
from cloudinary.models import CloudinaryField
from accounts.models import Profile
from django.utils.text import slugify


# Create your models here.
class TattooPost(models.Model):
    """
    Add ability to post tattoo images
    """
    title = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, max_length=255)
    date = models.DateField(auto_now_add=True)
    body = models.TextField(blank=True,
                            null=True,
                            max_length=500)
    image = CloudinaryField('image', default="https://res.cloudinary.com/dxsodecl1/image/upload/v1648317615/blank_jg5vze.jpg")
    author = models.ForeignKey(Profile, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    def info(self):
        return self.body

    def __init__(self, *args, **kwargs):
        super(TattooPost, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TattooPost, self).save(*args, **kwargs)
