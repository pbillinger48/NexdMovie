from django.shortcuts import render
from rest_framework import generics, status
from .serializers import MovieSerializer, CreateMovieSerializer, UserSerializer, CreateUserSerializer
from .models import Movie, User
from rest_framework.views import APIView
from rest_framework.response import Response

#Not currently used, would query all movies in db
class MovieView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
#Not currently used, would query all users in db
class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#The view that is called when a user is created, or searched in the main get movies input
#Creates user if not in db, and calls searched user if user already exists in db
class CreateUserView(APIView):
    serializer_class = CreateUserSerializer  
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            userName = serializer.data.get('userName')
            try:
                user = User.objects.get(userName=userName)
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                user = User(userName=userName)
                user.save()
                
                return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#View that is called to reset the user, looks at the current user name and resets the user with that user name and creates a new user object
#New user object allows recommendations to be recreated for more up to date results
#Currently relies on username in input field to stay the same, otherwise can run into some errors, upgraded way of working could  be useful in future
class RefreshUserView(APIView):
    serializer_class = CreateUserSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            userName = serializer.data.get('userName')
            try:
                user = User.objects.get(userName=userName)
                user.delete()
                user = User(userName=userName)
                user.save()
                
                return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
            except User.DoesNotExist:
                return Response({"message": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)       
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#View that gets user object in the username, and shows more recommendations 
#To get older recommendations back, refresh will have to be called
#Has same reliance on username, could be upgraded in future to prevent user errors
class GetMoreView(APIView):
    serializer_class = CreateUserSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            userName = serializer.data.get('userName')
            try:
                user = User.objects.get(userName=userName)
                user.getMore()
                user.save()
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"message": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Not currently used, could be used to create the movie object from the scraped data
class CreateMovieView(APIView):
    serializer_class = CreateMovieSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            title = serializer.data.get('title')
            rating = serializer.data.get('rating')
            movie = Movie(title = title, rating = rating)
            movie.save()
            return Response(UserSerializer(movie).data,status=status.HTTP_201_CREATED)