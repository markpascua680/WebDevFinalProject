from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to ='images/profile', blank=True) 
    first_name = models.CharField(('first_name'), max_length=150, blank=True)
    last_name = models.CharField(('last_name'), max_length=150, blank=True)
    pass

class MenuItem(models.Model):
    item_name = models.CharField(('item_name'), max_length=150, blank=False)
    star_rating = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    image = models.ImageField(upload_to ='images/menu_items', blank=True) 
    notes = models.TextField(('notes'), max_length=300, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", default=1)
    pass

class Restaurant(models.Model):
    name = models.CharField(('name'), max_length=25, blank=False)
    menu_items = models.ManyToManyField(MenuItem)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator", default=1)
    pass