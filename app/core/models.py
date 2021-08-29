from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

# Create your models here.


class CustomUserManager123(BaseUserManager):

    def create_user123(self, email, password=None, **extra_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError("email must be present")
        user123 = self.model(email=self.normalize_email(email), **extra_fields)  # normalize the email address by lowercasing the domain part of i
        user123.set_password(password)
        # user123.save(using=self._db)
        user123.save()
        return user123

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user456 = self.create_user123(email, password)
        user456.is_staff = True
        user456.is_superuser = True
        user456.save(using=self._db)
        return user456

class CustomUser111(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects123 = CustomUserManager123()

    USERNAME_FIELD = 'email'


