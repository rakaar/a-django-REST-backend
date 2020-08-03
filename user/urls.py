from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('verify/<str:hashed_code>/', views.Verify.as_view(), name='verify'),
    path('forgot/', views.ForgotPassword.as_view(), name='forgot_password'),
    path('reset/', views.ResetPassword.as_view(), name='reset_password'),
    path('google/', views.GoogleOAuth.as_view(), name='google'),
    path('linkedin/', views.LinkedinOAuth.as_view(), name='linkedin-oauth'),
    path('apple/<str:sub>', views.AppleUserToProfile, name='apple-profile'),
    path('group/recent/', views.ReadBy.as_view(), name='recent'),
    path('newsletter/', views.NewsLetter.as_view(), name='news_letter')
]
