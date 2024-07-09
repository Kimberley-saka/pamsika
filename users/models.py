"""
defines user class
"""
from django.db import models
from django.contrib.auth.models import AbstractUser



class Users(AbstractUser):
    pass



    class Meta:

        db_table = 'users'
        """
        define table name
        """

        db_table = 'users'
