from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_field):
        """Create and save a new user"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user models that suport email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    ROLE_CHOICES = (
        (1, 'admin'),
        (2, 'supervisor'),
        (3, 'distributor'),
    )
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, default='3')

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Remittance(models.Model):
    """Remittance model"""
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField(max_length=255)
    recipients_name = models.CharField(max_length=255)
    delivery_address = models.TextField()
    recipients_phone = models.CharField(max_length=11)
    recipients_id = models.CharField(max_length=11)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    STATUSES = (
        ('i', 'Initiated'),
        ('a', 'Assigned'),
        ('d', 'Delivered'),
        ('c', 'Cancelled'),
    )
    status = models.CharField(choices=STATUSES, default='i', max_length=10)
    initialization_date = models.DateTimeField(auto_now_add=True)
    assignment_date = models.DateTimeField(default=None, null=True, blank=True)
    delivery_date = models.DateTimeField(default=None, null=True, blank=True)
    distributor = models.ForeignKey(
        'User', on_delete=models.PROTECT, default=None, null=True, blank=True)
