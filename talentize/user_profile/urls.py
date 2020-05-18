from django.urls import path
from . import views

urlpatterns = [
    path('', views.Profile.as_view(), name='get_profile'),
    path('education/', views.Education.as_view(), name='education'),
    path('achs/', views.Achievement.as_view(), name='achs')

]
