# Generated by Django 3.1.7 on 2021-03-04 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210302_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='site',
            field=models.URLField(blank=True, max_length=228, null=True),
        ),
    ]
