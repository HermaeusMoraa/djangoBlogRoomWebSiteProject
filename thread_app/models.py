from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from user_app.models import CustomUserAccountModel
from taggit.managers import TaggableManager



class TimeStampedModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True




class CategoryModel(models.Model):
	name = models.CharField(max_length=100, unique=True)
	def __str__(self):
		return self.name






# class TagModel(models.Model):
# 	name = models.CharField(max_length=50, unique=True)
# 	def __str__(self):
# 		return self.name




class ThreadModel(TimeStampedModel):

	title = models.CharField(max_length=100)
	description = models.TextField(max_length=1000, blank=True, null=True)
	image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)

	#FK
	creator = models.ForeignKey(CustomUserAccountModel, on_delete=models.CASCADE)
	category = models.ForeignKey(CategoryModel, on_delete=models.SET_DEFAULT, default=None)

	### TAG PROBLEM ###
	# tag = models.ManyToManyField(TagModel, related_name='threads_model')
	tags = TaggableManager()
	def __str__(self):
		return f'Thread title: {self.title}, description: {self.description}'

	def get_absolute_url(self):
		return reverse('thread-detail', kwargs={'pk': self.pk})

	def like_count(self):
		return self.likes.count()



class CommentModel(TimeStampedModel):

	text = models.TextField(max_length=1000)

	thread_link = models.ForeignKey(ThreadModel, related_name='comment_model', on_delete=models.CASCADE)
	user = models.ForeignKey(CustomUserAccountModel, on_delete=models.CASCADE)
	def __str__(self):
		return self.text[:50]

	def like_count(self):
		return self.likes.count()