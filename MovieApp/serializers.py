from rest_framework import serializers
from .models import Movie, User
#Not used currently, would serialize movies that are searched for in db
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('TmDbid', 'title', 'release_date', 'overview', 'popularity', 
                  'poster_path', 'vote_average', 'rating','cast', 'crew')
        
#Not currently used
#Serializes the user if a user object was called or searched for
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userName', 'user_films_dict' ,'movie_reccs_dict', 'reccs_info_dict')

#Serializer that is used to pass username from front to back end
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userName',)

#Not currently used, would be used to add movie objects to db
class CreateMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'rating')