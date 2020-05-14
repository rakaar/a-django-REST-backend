from django.db import models

class User(models.Model):
    name = models.CharField(blank=False, max_length=200)
    email = models.EmailField(blank=False)
    insti_email = models.EmailField(blank=True, max_length=100)
    password_hash = models.CharField(blank=False, max_length=300)
    
    def __str__(self):
        return self.name