from django.db import models
from django.utils import timezone
from .utils import *

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    birth_date = models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    apt = models.CharField(max_length=2)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=15)
    zip = models.CharField(max_length=5)
    salt = models.CharField(max_length=16, default=generate_salt)
    failed_logins = models.IntegerField(default=0)
    locked_out_until = models.DateTimeField(default=timezone.now)