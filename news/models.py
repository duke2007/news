from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date= models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def published(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title
        
        
class Post1(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title1 = models.CharField(max_length=200)
	text = models.TextField()
	created_date= models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def published(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title1


class Editorial(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	edit_title = models.CharField(max_length=200)
	edit_text = models.TextField()
	slug = models.CharField(max_length=70, default=False)
	edit_created_date= models.DateTimeField(default=timezone.now)
	edit_published_date = models.DateTimeField(blank=True, null=True)
	
	def published(self):
		self.edit_published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.edit_title