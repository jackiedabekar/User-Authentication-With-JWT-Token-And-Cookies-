from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class User(AbstractUser):
    name = models.CharField(max_length=20, null=False,blank=False)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ('-id',)

    def __str__(self) -> str:
        return self.name

