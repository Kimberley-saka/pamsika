"""
defines user class
"""
from django.db import models
from django.contrib.auth.models import AbstractUser



class Users(AbstractUser):
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
    
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
   
        return self.is_admin


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
