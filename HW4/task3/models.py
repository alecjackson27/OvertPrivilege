from django.db import models

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

    def signup(self):
        # Add validation from task 1 and 2 here before creating new user

        # If password is validated successfully, save user in database and send password 
        # to password file

        self.save()