from django.urls import path
from .views import get_user, create_user, get_users

urlpatterns = [
    path('users/', get_user, name='get_user'),
    path('users/create', create_user, name='create_user'),
    path('users/all', get_users, name='get_users'),
]