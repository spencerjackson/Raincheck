from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
	start_time = models.DateTimeField('when event starts')
	end_time = models.DateTimeField('when event finishes')
	title = models.CharField(max_length=200)
	description = models.TextField()
	creator = models.ForeignKey(User)
