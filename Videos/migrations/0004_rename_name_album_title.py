# Generated by Django 3.2.4 on 2021-12-11 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Videos', '0003_auto_20211211_0431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='name',
            new_name='title',
        ),
    ]
