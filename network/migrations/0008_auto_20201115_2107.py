# Generated by Django 3.1.1 on 2020-11-15 20:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_auto_20201115_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Follower',
            field=models.ManyToManyField(blank=True, default=0, related_name='_user_Follower_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
