from django.db import models

from thread_app.models import ThreadModel, CommentModel
from user_app.models import CustomUserAccountModel


class TimeStampedModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True


class ThreadLikeModel(TimeStampedModel):
	thread_link = models.ForeignKey(ThreadModel, related_name='likes', on_delete=models.CASCADE)
	user = models.ForeignKey(CustomUserAccountModel, related_name='user_thread_likes', on_delete=models.CASCADE)

	class Meta:
		unique_together = ('user', 'thread_link')

	def __str__(self):
		return f'{self.user.username} liked {self.thread_link.title}'



class CommentLikeModel(TimeStampedModel):
	comment_link = models.ForeignKey(CommentModel, related_name='likes', on_delete=models.CASCADE)
	user = models.ForeignKey(CustomUserAccountModel, related_name='user_comment_likes', on_delete=models.CASCADE)

	class Meta:
		unique_together = ('user', 'comment_link')

	def __str__(self):
		return f'{self.user.username} liked comment {self.comment_link.text[:20]}'


class SavedThreadModel(TimeStampedModel):
	thread_link = models.ForeignKey(ThreadModel, on_delete=models.CASCADE, related_name='saved_threads')
	user = models.ForeignKey(CustomUserAccountModel, on_delete=models.CASCADE, related_name='saved_by')

	def __str__(self):
		return f'{self.user.username} saved {self.thread_link.title}'

