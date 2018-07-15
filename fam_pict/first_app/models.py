from django.db import models
from django import forms
from django.core import validators
from django.contrib.auth.models import User
# Create your models here.

class FamilyMembers(models.Model):
    first_name = models.CharField(max_length=124)
    last_name = models.CharField(max_length=124)

class SignUp(models.Model):
    name = models.CharField(max_length=124)
    email = models.EmailField(max_length=124)
    verify_email = models.EmailField(max_length=124)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
