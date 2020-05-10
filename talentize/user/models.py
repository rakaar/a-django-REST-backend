from django.db import models

# Create your models here.
class User(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False)
    password_hash = models.CharField(blank=False, max_length=25)
    linkedin_handle = models.CharField(blank=False, max_length=50)