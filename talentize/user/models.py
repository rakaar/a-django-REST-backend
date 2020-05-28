from djongo import models
from user_profile.models import Profile


class User(models.Model):
    name = models.CharField(blank=False, max_length=200)
    email = models.EmailField(blank=False)
    insti_email = models.EmailField(blank=True, max_length=100)
    password_hash = models.CharField(blank=False, max_length=300)
    profile = models.EmbeddedField(blank=True, model_container=Profile)
    mesibo_uid = models.CharField(blank=True, max_length=100)
    mesibo_token = models.CharField(blank=True, max_length=100)
    
    def __str__(self):
        return self.name
