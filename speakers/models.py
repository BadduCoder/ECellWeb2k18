from django.db import models

# Create your models here.
class Speaker(models.Model):
	name = models.CharField(max_length=256, unique=True)
	company = models.CharField(max_length=256)
	year = models.IntegerField()
	profile_pic = models.ImageField(upload_to='static/uploads/speakers')
	email = models.EmailField(unique=True)
	contact = models.TextField(max_length=13, null=True, blank=True)
	description = models.TextField(default='none')
	year = models.IntegerField(default=2018)
	social_media = models.TextField(default='blank')
	# response = models.BooleanField(default=False)
	flag = models.BooleanField(default=False)
	designation = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name
		