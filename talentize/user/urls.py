from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('verify/<str:hashed_code>/', views.Verify.as_view(), name='verify'),
    path('google/', views.GoogleOAuth.as_view(), name='google'),
    path('apple/redirect/', views.AppleOAuth, name='apple-oauth'),
    path('apple/<str:sub>', views.AppleUserToProfile, name='apple-profile'),
    path('group/recent', views.ReadBy.as_view(), name='recent')
]