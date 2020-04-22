from django.db import models


class Client(models.Model):
	name = models.CharField(max_length=255)
	details = models.TextField()

class Doubt(models.Model):
	ask = models.CharField(max_length=255)
	response = models.TextField()
	

class Description(models.Model):
	title = models.CharField(max_length=255)
	details = models.TextField()

class PhotoProdutoAfterBefore(models.Model):
	name = models.CharField(max_length=255)
	photo = models.ImageField(upload_to='case', null=True)

	def __str__(self):
		return self.name