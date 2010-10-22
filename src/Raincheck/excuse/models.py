from django.db import models

# Create your models here.
class Excuse(models.Model):
	text = models.TextField()
