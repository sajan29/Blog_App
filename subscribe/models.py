from django.db import models

# Create your models here.
class Emails(models.Model):

	email=models.CharField(max_length=100,unique=True)
	subscribed=models.DateTimeField(auto_now_add=True)
	#Default Manager
	#objects=models.Manager()
	def __str__(self):
		return self.email
