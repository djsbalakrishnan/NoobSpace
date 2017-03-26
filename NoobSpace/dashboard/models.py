from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Posts(models.Model):
	#autoid is default
	name = models.CharField(max_length=30)
	tag = models.CharField(max_length=20)
	description = models.CharField(max_length=1000)
	url = models.CharField(max_length=250)
	datetime = models.DateField()