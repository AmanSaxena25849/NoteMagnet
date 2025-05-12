from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from notes.models import Notes


# Create your models here.

class users(AbstractUser):
    age = models.PositiveIntegerField(validators=[MinValueValidator(9), MaxValueValidator(110)], null=True)
    phone_number = PhoneNumberField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    notifications = models.BooleanField(default=False)
    varified = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='user_profile_image', blank=True, null=True)
    bookmark = models.ManyToManyField(Notes, related_name="User")
    
    
    def __str__(self):
        return self.username
    
