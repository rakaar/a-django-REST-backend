from django.urls import path
from . import views

url_patterns = [
    path('get_profile', views.Profile.as_view(), name='get_profile'),
]
