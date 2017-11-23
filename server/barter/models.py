from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Item(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
