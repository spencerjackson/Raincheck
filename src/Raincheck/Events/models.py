# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from Raincheck.Locations.models import Locations

class Event(models.Model):
    start_time = models.DateTimeField('when event starts')
    end_time = models.DateTimeField('when event finishes')
    title = models.CharField(max_length=200)
    description = models.TextField()
    creator = models.ForeignKey(User)
    location = models.ForeignKey(Locations)
    provider = models.CharField(max_length=200)
    def __str__(self):
     return title+" at "+location+" by "+creator.username
