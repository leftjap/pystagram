# coding: utf-8

from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    gender = models.CharField(max_length=1)