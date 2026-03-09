from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.users.managers import CustomUserManager


# Create your models here.

class User(AbstractUser):
    username = None
    email = None

    phone = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone

class UserProfile(models.Model):
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default="",
        blank=True
    )
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255)

    @property
    def phone(self):
        return self.user.phone

    def __str__(self):
        return f"{self.first_name} {self.last_name}"