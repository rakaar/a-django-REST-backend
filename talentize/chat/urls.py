from django.urls import path
from . import views

urlpatterns = [
    path('group/<int:gid>/', views.MesiboGroup.as_view(), name='mesibo_group_get'),
    path('group/', views.MesiboGroup.as_view(), name='mesibo_group'),
    path('user/<str:email>/', views.MesiboUser.as_view(), name='mesibo_user_get'),
    path('user/', views.MesiboUser.as_view(), name='mesibo_user'),
]
