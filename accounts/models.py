from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import JSONField


# Create your models here.

class users(AbstractUser):
    age = models.PositiveIntegerField(validators=[MinValueValidator(9), MaxValueValidator(110)])
    phone_number = PhoneNumberField(unique=True)
    bio = models.TextField(blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True)
    notifications = models.BooleanField(default=False)
    varified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username