# Generated by Django 3.1.1 on 2020-11-15 20:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_auto_20201115_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Follower',
            field=models.ManyToManyField(default=0, null=True, related_name='_user_Follower_+', to=settings.AUTH_USER_MODEL),
        ),
    ]