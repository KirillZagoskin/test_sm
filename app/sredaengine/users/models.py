from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.

class User(AbstractUser):
    link = models.SlugField(max_length=250, null=True)
    tg_id = models.PositiveIntegerField(null=True)

    def get_absolute_url(self):
        return reverse("user_page", kwargs={"username": self.username})
     