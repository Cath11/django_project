from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser (AbstractUser):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, default="Tell the readers a bit about YOU")
    profile_img = models.URLField(max_length=200, default="https://image.flaticon.com/icons/svg/545/545837.svg")
    
    
    # def __str__(self):
    #     return self.username

