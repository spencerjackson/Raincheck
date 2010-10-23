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
    type = models.CharField(max_length=1, choices=TYPE_OF_EXCUSE)
    author = models.ForeignKey(User)
    date = models.DateTimeField()
    def __str__(self):
      return self.author.username+" "+self.date.__str__()
    def get_liked(self):
      return self.likedBy.count()
    def get_disliked(self):
      return self.dislikedBy.count()

class ExcuseVote(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    like = models.ManyToManyField(Excuse, related_name="likedBy")
    dislike = models.ManyToManyField(Excuse, related_name="dislikedBy")
    def __str__(self):
      return self.user.username
