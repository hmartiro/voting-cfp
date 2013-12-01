from django.db import models

# Create your models here.

class Voter(models.Model):

	name = models.CharField(max_length=40)

	def __unicode__(self):
		return u"%s" % (self.name)

class Discussion(models.Model):

	name = models.CharField(max_length=60)
	description = models.TextField(max_length=200, blank=True)
	active = models.BooleanField(default=True)
	
	def __unicode__(self):
		return u"%s" % (self.name)

class Vote(models.Model):

	# Vote value:
	# For a binary vote, +1.0 or -1.0
	# For a continuous vote, [-1.0:+1.0] range
	value = models.FloatField()

	voter = models.ForeignKey(Voter)
	discussion = models.ForeignKey(Discussion)

	time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u"%s voted %s during %s discussion at %s" % (self.voter, self.value, self.discussion, self.time)
