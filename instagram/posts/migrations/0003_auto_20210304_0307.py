# Generated by Django 3.1.7 on 2021-03-04 03:07

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210304_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(upload_to=posts.models.upload_image),
        ),
    ]
