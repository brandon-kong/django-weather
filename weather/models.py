from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.utils import timezone

# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email
    

class SavedLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city + ", " + self.country