# Create your models here.
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
import datetime
class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField('when event starts')
    end_time = models.DateTimeField('when event finishes')
    description = models.TextField()
    creator = models.ForeignKey(User)
    provider = models.CharField(max_length=200)
    def __str__(self):
     return title+" at "+location+" by "+creator.username
    def start_date(self):
        return "new Date(%s,%s,%s)"%(self.start_time.year, self.start_time.month-1, self.start_time.day)
    def end_date(self):
        self.end_time -= datetime.timedelta(seconds=1)
        return "new Date(%s,%s,%s)"%(self.end_time.year, self.end_time.month-1, self.end_time.day)

class EventForm(ModelForm):
	start_time = models.DateTimeField(default = "year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]")
	end_time = models.DateTimeField(default = "year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]")
	class Meta:
		model = Event
