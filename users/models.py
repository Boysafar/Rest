from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import OneToOneField

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram = models.URLField(null=True, blank=True)
    bio = models.CharField(max_length=250)

    age = models.IntegerField(null=True, blank=True)

    def __str__(self) -> OneToOneField:
        return self.user.first_name


