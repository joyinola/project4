# Generated by Django 3.1.1 on 2020-12-18 16:11

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0015_auto_20201218_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='Img',
            field=models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='/media/Post_img'), upload_to=''),
        ),
    ]
