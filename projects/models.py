from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

"""class Data(models.Model):
    project_name = models.CharField(max_length=250)
    creater = models.ForeignKey(settings.AUTH_USER_MODEL)
    discription = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('analyse:index')

    def __str__(self):
        return self.table_name
"""