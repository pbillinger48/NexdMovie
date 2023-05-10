from django.urls import path
from.views import UserView, CreateUserView, RefreshUserView, GetMoreView
#What sets the names for the api calls that will be used in react
urlpatterns = [
    path('user', UserView.as_view()),
    path('create-user', CreateUserView.as_view()),
    path('refresh-user', RefreshUserView.as_view()),
    path('get-more', GetMoreView.as_view())
]