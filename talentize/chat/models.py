from djongo import models


class Group(models.Model):
    gid = models.IntegerField(blank=False)
    uni_ids = models.ArrayField(model_container=models.EmailField, blank=True)
    name = models.CharField(max_length=200, blank=True)
