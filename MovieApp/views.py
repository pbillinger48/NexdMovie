from django.shortcuts import render
from rest_framework import generics, status
from .serializers import MovieSerializer, CreateMovieSerializer, UserSerializer, CreateUserSerializer
from .models import Movie, User
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class MovieView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserView(APIView):
    serializer_class = CreateUserSerializer
    def post(self, request, format= None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            userName = serializer.data.get('userName')
            user = User(userName = userName)
            user.save()
            return Response(UserSerializer(user).data,status=status.HTTP_201_CREATED)
        

class CreateMovieView(APIView):
    serializer_class = CreateMovieSerializer
    def post(self, request, format=None):
        pass