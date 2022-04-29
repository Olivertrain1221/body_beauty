from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    """
    Main Model for the users profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', default="https://res.cloudinary.com/dxsodecl1/image/upload/v1648317615/blank_jg5vze.jpg")
    

    def __str__(self):
        return f'{self.user.username}'
