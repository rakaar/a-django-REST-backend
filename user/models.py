from djongo import models
from user_profile.models import Profile
from chat.models import Mail

class LastSeen(models.Model):
    mid = models.IntegerField(blank=True)
    flag = models.CharField(max_length=10,blank=True)
    uni_ids = models.ArrayField(model_container=Mail, blank=True)

class MesiboGroup(models.Model):
    gid = models.IntegerField(blank=True)
    status = models.BooleanField(blank=True)
    last_seen_msgs = models.ArrayField(model_container=LastSeen,blank=True)    

class MesiboUser(models.Model):
    uid = models.CharField(blank=True, max_length=100)
    access_token = models.CharField(blank=True, max_length=100)
    groups = models.ArrayField(model_container=MesiboGroup, blank=True)

class User(models.Model):
    name = models.CharField(blank=False, max_length=200)
    email = models.EmailField(blank=False)
    insti_email = models.EmailField(blank=True, max_length=100)
    password_hash = models.CharField(blank=False, max_length=300)
    profile = models.EmbeddedField(blank=True, model_container=Profile)
    mesibo_details = models.EmbeddedField(
        blank=True, model_container=MesiboUser)

    def __str__(self):
        return self.name
