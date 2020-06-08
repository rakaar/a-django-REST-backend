from djongo import models


class Mail(models.Model):
    email = models.EmailField(blank=True)

class MsgReferBy(models.Model):
	refer_by = models.IntegerField(blank=True)

class MsgRefer(models.Model):
	refer_to = models.IntegerField(blank=True)
	refer_by = models.ArrayField(model_container=MsgReferBy, blank=True)

class Group(models.Model):
    gid = models.IntegerField(blank=False)
    uni_ids = models.ArrayField(model_container=Mail, blank=True)
    name = models.CharField(max_length=200, blank=True)
    msg_refers = models.ArrayField(model_container=MsgRefer, blank=True)



