from django.db import models

# Create your models here.
class Movie(models.Model):
    tmdbID = models.CharField(max_length=4, default="0")
    title = models.CharField(max_length=50, default="No Ttle")

class User(models.Model):
    userName = models.CharField(max_length=30, default="defaultUsername")