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