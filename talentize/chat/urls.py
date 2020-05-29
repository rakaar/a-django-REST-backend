from django.urls import path
from . import views

url_patterns = [
    path('group/', views.MesiboGroup.as_view(), name='group')
]
