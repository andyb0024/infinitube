# Generated by Django 3.2.4 on 2021-12-11 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Videos', '0002_auto_20211211_0417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artiste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artiste',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='Videos.artiste'),
        ),
    ]