from rest_framework import serializers
from .models import Movie, User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('TmDbid', 'title', 'release_date', 'overview', 'popularity', 
                  'poster_path', 'vote_average', 'rating','cast', 'crew')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userName', 'user_films_dict' ,'movie_reccs_dict', 'reccs_info_dict')

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userName',)


class CreateMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'rating')