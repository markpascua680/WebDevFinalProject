from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class User(AbstractUser):
    pass

class MenuItem(models.Model):
   item_name = models.CharField(('item_name'), max_length=150, blank=False, unique=True)
   star_rating = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
   image = models.ImageField(upload_to ='uploads/') 
   notes = models.TextField(('notes'), max_length=300, blank=True)
   pass

class Restaurant(models.Model):
    name = models.CharField(('name'), max_length=25, blank=False, unique=True)
    menu_items = models.ManyToManyField(MenuItem)
    pass