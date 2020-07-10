from django.db import models

# Create your models here.
class repair_request(models.Model):
	name = models.CharField(max_length=100)
	number = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	message = models.TextField(max_length=500, blank=True)

	def __str__(self):
		return self.name

class new_client(models.Model):
	name = models.CharField(max_length=100)
	number = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	message = models.TextField(max_length=500, blank=True)


	def __str__(self):
		return self.name

