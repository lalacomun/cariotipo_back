from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

class cariotipo(models.Model):

    imagen = models.FileField(null=True,blank=True)
    
    imagen2 = models.FileField(null=True,blank=True)

    def __unicode__(self):
        return '{}'.format(str(self.id))

class userprofile(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __unicode__(self):
        return '{}'.format(str(self.id))

