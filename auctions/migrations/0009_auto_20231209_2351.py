# Generated by Django 3.2.21 on 2023-12-10 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_restaurant_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='item_name',
            field=models.CharField(max_length=150, unique=True, verbose_name='item_name'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='notes',
            field=models.TextField(max_length=300, verbose_name='notes'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=25, unique=True, verbose_name='name'),
        ),
    ]