from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=False)
    number = models.CharField(max_length=13, null=True, blank=False)
