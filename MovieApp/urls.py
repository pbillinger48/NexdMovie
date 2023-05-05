from django.urls import path
from.views import UserView, CreateUserView, RefreshUserView, GetMoreView

urlpatterns = [
    path('user', UserView.as_view()),
    path('create-user', CreateUserView.as_view()),
    path('refresh-user', RefreshUserView.as_view()),
    path('get-more', GetMoreView.as_view())
]