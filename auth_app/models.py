from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100,null=True,blank=True)
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []
    # email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    mobilenumber = models.CharField(max_length=32)
    email = models.EmailField(max_length=100, blank=True, null=True)
    location = models.CharField(blank=True, max_length=100)
    address = models.CharField(blank=True, max_length=200)
