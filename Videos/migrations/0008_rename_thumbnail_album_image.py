# Generated by Django 3.2.4 on 2021-12-11 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Videos', '0007_album_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='thumbnail',
            new_name='image',
        ),
    ]
