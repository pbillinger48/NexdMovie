from django.db import models
from .Scraper import get_user_films_dict



# Create your models here.
class Movie(models.Model):
    tmdbID = models.CharField(max_length=4, default="0")
    title = models.CharField(max_length=50, default="No Title")

class User(models.Model):
    userName = models.CharField(max_length=30, default="defaultUsername")
    user_films_dict = models.JSONField(default=dict)
    def save(self, *args, **kwargs):
        self.user_films_dict = get_user_films_dict(self.userName)
        super().save(*args, **kwargs)