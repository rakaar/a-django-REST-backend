from django.urls import path
from . import views

url_patterns = [
    path('group/', views.Group.as_view(), name='group')
]
