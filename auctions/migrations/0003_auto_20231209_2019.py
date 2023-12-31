# Generated by Django 3.2.21 on 2023-12-10 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20231030_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150, verbose_name='item_name')),
                ('star_rating', models.PositiveIntegerField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('notes', models.TextField(max_length=300, verbose_name='notes')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('category', models.CharField(max_length=150, verbose_name='category')),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='item',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='author',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='item',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='user',
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Listing',
        ),
        migrations.DeleteModel(
            name='Watchlist',
        ),
    ]
