from xml.etree.ElementTree import Comment
from django import forms
from django.core.exceptions import ValidationError

from .models import Restaurant, MenuItem
class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ('name',)
        labels = {
            'name': 'Restaurant Name',
        }

class MenuItemForm(forms.ModelForm):

    class Meta:
        model = MenuItem
        fields = ('item_name', 'star_rating', 'image', 'notes')
        labels = {
            'item_name': 'Name of Food',
            'star_rating': 'How delicious was it on a scale of 0-5?',
            'notes': 'What did you think about it?'
        }