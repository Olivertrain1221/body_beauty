from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    """
    Main Model for the users profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='blank.jpg',
                                      upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}'
