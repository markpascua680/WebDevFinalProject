# Generated by Django 3.2.22 on 2023-12-11 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0029_auto_20231210_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='creator',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
