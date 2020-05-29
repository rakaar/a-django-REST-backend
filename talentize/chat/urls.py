from django.urls import path
from . import views

urlpatterns = [
    path('group/', views.Group.as_view(), name='group'),
]
