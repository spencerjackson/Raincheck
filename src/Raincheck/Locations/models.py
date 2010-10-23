from django.db import models

# Create your models here.

class Locations(models.Model):
	location = models.CharField(max_length=200)
