<<<<<<< HEAD
from django.db import models

# Create your models here.
=======
"""
defines user class
"""
from django.db import models
from django.contrib.auth.models import AbstractUser



class Users(AbstractUser):
    """
    user
    """

    password = models.CharField(max_length=255)


    USERNAME_FIELD = 'email'





    class Meta:
        """
        define table name
        """

        db_table = 'users'
>>>>>>> 57660b55b1c9146ca4428259680c3f0e31e2b370
