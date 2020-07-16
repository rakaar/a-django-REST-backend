from django.urls import path
from . import views

urlpatterns = [
    path('', views.Profile.as_view(), name='get_profile'),
    path('education', views.Education.as_view(), name='education'),
    path('experience', views.Experience.as_view(), name='experience'),
    path('achs/', views.Achievement.as_view(), name='achs'),
    path('personal/', views.Personal.as_view(), name='personal'),
    path('pic/', views.ProPic.as_view(), name='propic')
]
