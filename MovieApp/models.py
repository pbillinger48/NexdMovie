from django.db import models
from django.contrib.postgres.fields import ArrayField
from .Scraper import get_user_films_dict, get_Positive_user_films_dict, get_user_films_dict_optimized
import requests
import json
from .EZReccomender import get_reccomendations, getRecInfo

TMDB_API_KEY = 'a497a7718fd66875ff47bd0a20cd4b24'

# Create your models here.
#Not used in current iteration of project
class Movie(models.Model):
    TmDbid = models.CharField(max_length=8, default="0", blank = True)
    title = models.CharField(max_length=100, default="No Title")
    release_date = models.CharField(max_length=32, default="No Date")
    overview = models.CharField(max_length=500, default="")
    popularity= models.IntegerField(null=False, default=0)
    poster_path = models.CharField(max_length=1000, default="")
    #genre_ids = ArrayField(models.IntegerField())
    rating = models.IntegerField(null = False, default=0)
    vote_average = models.IntegerField(null = False, default=0)
    cast = models.JSONField(default=list)
    crew = models.JSONField(default=list)

    def __str__(self):
        return self.title

    def gather_info_and_credits(self):
        self.title.replace( '_', ':')
        url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={self.title}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['total_results'] > 0:
                # Return the first result
                data = data['results'][0] 
            if 'id' in data:
                self.TmDbid = data['id']
            else:
                self.TmDbid = 0
            if data.get('title'):               
                self.title = data.get('title')
            if data.get('release_date'):
                self.release_date = data.get('release_date')
            if data.get('overview'):
                self.overview = data.get('overview')
            if data.get('popularity'):
                self.popularity = data.get('popularity')
            if data.get('poster_path'):
                self.poster_path = data.get('poster_path')
            #self.genre_ids = data.get('genre_ids')
            if data.get('vote_average'):
                self.vote_average = data.get('vote_average')
            
            url2 = f'https://api.themoviedb.org/3/movie/{id}/credits?api_key={TMDB_API_KEY}'
            response = requests.get(url2)
            if response.status_code == 200:
                data = response.json()
                # Get the top 12 cast members
                self.cast = data['cast'][:12]
                # Get the crew members we're interested in
                self.crew = [member for member in data['crew'] if member['job'] in ['Director', 'Producer','Editor', 'Cinematography', 'Screenplay',
                                                                                'Art Direction', 'Casting', 'Composer', 'Executive Producer', 'Score', 'Original Music Composer']]
            
        self.save()

#Main User data object
#Holds username, dictionary of seen films, dictionary of recommendation titles, and dictionary of info for movies currently being displayed
class User(models.Model):
    userName = models.CharField(max_length=50, default="defaultUsername")
    user_films_dict = models.JSONField(default=dict)
    movie_reccs_dict = models.JSONField(default=dict)
    reccs_info_dict =models.JSONField(default=dict)
    #movies = models.ManyToManyField(Movie, related_name= 'movie_reccs')
    #moviereccs = models.ManyToManyField('Movie', related_name='reccomended_by')
    
    #This function controlls what happens when a user object is saved
    def save(self, *args, **kwargs):
        if self.pk is None:  # only execute this block if the user is new
            self.user_films_dict = get_user_films_dict_optimized(self.userName)
            self.movie_reccs_dict = get_reccomendations(self.user_films_dict)
            self.reccs_info_dict = getRecInfo(self.movie_reccs_dict, self.reccs_info_dict)
        super().save(*args, **kwargs)
    #This is the function that is called to update the user when the show more button is pressed
    def getMore(self):
        self.reccs_info_dict = getRecInfo(self.movie_reccs_dict, self.reccs_info_dict)
        self.save()
    #This function is for version of project with tracked movie objects    
    #def create_movie_list(self):
        #self.movies.clear()
        #self.moviereccs.clear()
       #for title, rating in self.user_films_dict.items():          
            #movie=Movie(title=title, rating=rating)
            #movie.gather_info_and_credits()
            #movie.save()
            #self.movies.add(movie)
        #for title, rating in self.movie_reccs_dict.items():           
            #movie=Movie(title=title, rating=rating)
            #movie.gather_info_and_credits()
            #movie.save()
            #self.moviereccs.add(movie)                 
          


        
