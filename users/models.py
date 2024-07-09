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
    pass



    class Meta:
<<<<<<< HEAD
        db_table = 'users'
=======
        """
        define table name
        """

        db_table = 'users'
>>>>>>> 57660b55b1c9146ca4428259680c3f0e31e2b370
>>>>>>> d7f273a07d20459610c54c481c3c1bb7af63d9e7
