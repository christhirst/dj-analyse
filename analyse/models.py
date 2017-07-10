from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.



def upload_location(instance, filename):
    return "%s/%s" %(instance.uploader, filename)



class Data(models.Model):
    table_name = models.CharField(max_length=250)
    album_logo = models.FileField(upload_to=upload_location)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL)
    discription = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('analyse:index')

    def __str__(self):
        return self.table_name

    #def __str__(self):
        #return self.album_logo.name


class Chemical(models.Model):
    chem_name = models.CharField(max_length=250)
