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
        db_table = 'users'