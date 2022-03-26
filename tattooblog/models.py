from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class TattooPost(models.Model):
    """
    Add ability to post tattoo images
    """
    title = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, max_length=255)
    date = models.DateField(auto_now_add=True)
    body = models.TextField(blank=True, null=True, max_length=50)
    image = CloudinaryField('image', default="https://res.cloudinary.com/dxsodecl1/image/upload/v1644248279/cld-sample.jpg")
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def info(self):
        return self.body
