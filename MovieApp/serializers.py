from rest_framework import serializers
from .models import Movie, User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'tmdbID', 'title')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userName')

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userName')


class CreateMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title')