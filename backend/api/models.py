from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from .storage import OverwriteStorage
import os

#this code should be in api/models but it doesn't work there Xd

class CustomUserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email: str, password: str, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
        
    #Won't use superuser option
    """
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
    """


def get_filepath(instance, filename):
    path = os.path.join(f"author_{instance.id}", f"avatar", "customAvatar.png")
    return path

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    join_date = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(default=r'default.png', upload_to=get_filepath, storage=OverwriteStorage())

    USERNAME_FIELD = "email" #ensures that email serves as an unique identifier for a user

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} ({self.email})"
    
    class Meta:
        abstract = False
        verbose_name = 'user'
        verbose_name_plural = 'users'





