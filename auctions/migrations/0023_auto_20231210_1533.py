# Generated by Django 3.2.22 on 2023-12-11 00:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_auto_20231210_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='restaurant',
            field=models.ManyToManyField(related_name='restaurant', to='auctions.Restaurant'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='creator',
            field=models.ManyToManyField(related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='menu_items',
            field=models.ManyToManyField(related_name='menu_items', to='auctions.MenuItem'),
        ),
    ]