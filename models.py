from django.db import models

class Blog(models.Model):
	name = models.CharField(max_length=32)
	date = models.DateTimeField(auto_now_add=True)
	feedback = models.CharField(max_length=32)

