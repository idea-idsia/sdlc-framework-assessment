## backend/users/urls.py

from django.urls import path
from .views import register_user, login_user, get_user_profile

urlpatterns = [
    path('register/', register_user, name='register-user'),
    path('login/', login_user, name='login-user'),
    path('profile/', get_user_profile, name='get-user-profile'),
]
