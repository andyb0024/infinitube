# Generated by Django 3.2.4 on 2021-12-11 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Videos', '0008_rename_thumbnail_album_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Videos.album'),
        ),
    ]
