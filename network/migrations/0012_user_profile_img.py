# Generated by Django 3.1.1 on 2020-12-14 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(default='profile.jpg', upload_to='profile_pics'),
        ),
    ]
