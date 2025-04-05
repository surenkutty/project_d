from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email= models.EmailField(unique=True)
    phone = models.CharField(max_length=13)
    address = models.TextField()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone']

    def __str__(self):
        return self.username

