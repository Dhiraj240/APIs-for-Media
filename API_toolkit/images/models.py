from django.db import models

# Create your models here.
class image(models.Model):
	identification = models.CharField(max_length = 100)
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 500)
	image = models.ImageField(upload_to = 'pictures')
	createdby = models.CharField(max_length = 100)

	def __str__(self):
		return self.identification