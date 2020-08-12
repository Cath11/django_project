from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser (AbstractUser):

    #profil pic
    #bio
    pass

    def __str__(self):
        return self.username

