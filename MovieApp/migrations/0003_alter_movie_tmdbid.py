# Generated by Django 4.1.5 on 2023-03-21 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0002_remove_movie_genre_ids_alter_movie_tmdbid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='TmDbid',
            field=models.CharField(blank=True, default='0', max_length=8),
        ),
    ]