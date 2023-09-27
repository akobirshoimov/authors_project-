from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class CustomUser(AbstractUser):
    CHOICE_ROLES = (
        (3,'admin'),
        (2,'staff'),
        (1,'user')
    ) 

    roles = models.IntegerField(choices=CHOICE_ROLES,default=3)
    