from django.urls import path
from . import views

urlpatterns = [
    path('group/', views.MesiboGroup.as_view(), name='group')
]
