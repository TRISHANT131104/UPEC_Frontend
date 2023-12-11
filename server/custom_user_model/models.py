from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser,
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
    User,
)

class User(AbstractUser):
    role = models.CharField(max_length=20, default='client')
    image = models.URLField(default=None,null=True,blank=True)
    class Meta:
      abstract = False