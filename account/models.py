from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_user = models.BooleanField(default=False, null=True, blank=True)
    profile_picture = models.ImageField(upload_to="images", default="")
