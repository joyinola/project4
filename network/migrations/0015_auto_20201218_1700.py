# Generated by Django 3.1.1 on 2020-12-18 16:00

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0014_auto_20201217_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='Img',
            field=models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='/media/Profile_img'), upload_to=''),
        ),
    ]