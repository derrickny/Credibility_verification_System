from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(unique=True,max_length=255,default="")
    email = models.EmailField(unique=True, default="")
    password = models.CharField(max_length=255)
    retype_password = models.CharField(max_length=255)

    def __str__(self):
        return self.username 

    