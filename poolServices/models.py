from django.db import models

class MonthlyService(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	image = models.ImageField(upload_to='poolServices/images/')

	def __str__(self):
		return self.title

class review(models.Model):
	name = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	comments = models.TextField(max_length=250, blank=True)
	

	def __str__(self):
		return self.name