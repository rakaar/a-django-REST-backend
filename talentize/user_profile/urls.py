from django.urls import path
from . import views

urlpatterns = [
    path('get_profile', views.Profile.as_view(), name='get_profile'),
    path('update_education', views.Education.as_view(), name='education')
]
