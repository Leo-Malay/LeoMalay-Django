from enum import unique
from django.db import models

# Create your models here.


class Account(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    country = models.CharField(max_length=5)
    email = models.CharField(max_length=50, unique=True)
    password = models.TextField()
    token = models.TextField()

    def __str__(self):
        return self.email
