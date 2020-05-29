from djongo import models


class Mail(models.Model):
    email = models.EmailField(blank=True)


class Group(models.Model):
    gid = models.IntegerField(blank=False)
    uni_ids = models.ArrayField(model_container=Mail, blank=True)
    name = models.CharField(max_length=200, blank=True)
