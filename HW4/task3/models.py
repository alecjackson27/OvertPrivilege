from django.db import models
from datetime import timezone, datetime

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    birth_date = models.DateField()
    street = models.CharField(max_length=50)
    apt = models.CharField(max_length=2)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=15)
    zip = models.PositiveIntegerField()
    failed_logins = models.IntegerField(default=0)
    locked_out_until = models.DateTimeField(default="1970-01-01 11:11")