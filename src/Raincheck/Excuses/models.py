from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Excuse(models.Model):
    TYPE_OF_EXCUSE = (
	('I', 'Illness'),
	('P', 'Personal'),
	('W', 'Work'),
	('F', 'Funny')
    )
    text = models.TextField()
    excuse = models.CharField(max_length=1, choices=TYPE_OF_EXCUSE)
    author = models.ForeignKey(User)
    like = models.IntegerField()
    dislike = models.IntegerField()
    date = models.DateTimeField()
