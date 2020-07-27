from djongo import models

def upload_path_person(instance, filename):
    return '/'.join(['person_pic', filename])
    

class Experience(models.Model):
    detail = models.CharField(max_length=3000, blank=False)

class Resource(models.Model):
    title = models.CharField(max_length=500, blank=False)
    link = models.CharField(max_length=5000, blank=False)
    level = models.CharField(max_length=50 , blank=False)
    tags = models.CharField(max_length=1000, blank=False)
    description = models.CharField(max_length=5000, blank=True)
    cover = models.CharField(max_length=1000,blank=True)

class LearnerList(models.Model):
    person_name = models.CharField(max_length=200, blank=False)
    person_pic = models.ImageField(blank=True, null=True,upload_to=upload_path_person)
    category = models.CharField(max_length=2000, blank=False)
    experience = models.ArrayField(model_container=Experience, blank=False)
    podcast = models.CharField(max_length=5000, blank=True)
    resources = models.ArrayField(model_container=Resource, blank=True)

