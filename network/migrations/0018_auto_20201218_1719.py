# Generated by Django 3.1.1 on 2020-12-18 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0017_auto_20201218_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='Img',
            field=models.ImageField(blank=True, upload_to='Post_img'),
        ),
    ]