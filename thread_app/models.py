from django.db import models
from user_app.models import CustomUserModel
from taggit.managers import TaggableManager


class CategoryModel(models.Model):
	name = models.CharField(max_length=100, unique=True)
	def __str__(self):
		return self.name



# class TagModel(models.Model):
# 	name = models.CharField(max_length=50, unique=True)
# 	def __str__(self):
# 		return self.name




class ThreadModel(models.Model):

	title = models.CharField(max_length=100)
	description = models.TextField(max_length=1000)

	#FK
	creator = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
	category = models.ForeignKey(CategoryModel, on_delete=models.SET_DEFAULT, default=None)
	# tag = models.ManyToManyField(TagModel, related_name='threads_model')
	tags = TaggableManager()
	def __str__(self):
		return f'Thread title: {self.title}, description: {self.description}'





class CommentModel(models.Model):

	text = models.TextField(max_length=1000)

	thread_link = models.ForeignKey(ThreadModel, related_name='comment_model', on_delete=models.CASCADE)
	commentator = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
	def __str__(self):
		return self.text[:50]