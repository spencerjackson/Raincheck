# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Excuse(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User)