# Generated by Django 3.2.21 on 2023-12-10 09:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_menuitem_star_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='star_rating',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
