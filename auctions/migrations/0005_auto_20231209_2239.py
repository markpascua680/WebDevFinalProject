# Generated by Django 3.2.21 on 2023-12-10 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20231209_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuisine',
            name='cuisine',
            field=models.CharField(blank=True, max_length=150, verbose_name='cuisine'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='cuisine',
            field=models.ManyToManyField(blank=True, to='auctions.Cuisine'),
        ),
    ]
