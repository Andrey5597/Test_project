# Generated by Django 2.1.5 on 2019-12-12 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foto_album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foto_album.Album'),
        ),
    ]
