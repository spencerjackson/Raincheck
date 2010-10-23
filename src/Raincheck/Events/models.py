# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from Raincheck.Locations.models import Locations
import datetime
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
    def start_date(self):
        return "new Date(%s,%s,%s)"%(self.start_time.year, self.start_time.month-1, self.start_time.day)
    def end_date(self):
        self.end_time -= datetime.timedelta(seconds=1)
        return "new Date(%s,%s,%s)"%(self.end_time.year, self.end_time.month-1, self.end_time.day)
