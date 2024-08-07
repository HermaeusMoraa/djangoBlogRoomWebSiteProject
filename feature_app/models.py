from django.db import models

from thread_app.models import ThreadModel, CommentModel
from user_app.models import CustomUserAccountModel


class TimeStampedModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class ThreadLikeModel(TimeStampedModel):
	thread_link = models.ForeignKey(ThreadModel, related_name='likes', on_delete=models.CASCADE)
	user = models.ForeignKey(CustomUserAccountModel, related_name='thread_likes', on_delete=models.CASCADE)

	class Meta:
		unique_together = ('thread_link', 'user')



class CommentLikeModel(TimeStampedModel):
	comment_link = models.ForeignKey(CommentModel, related_name='likes', on_delete=models.CASCADE)
	user = models.ForeignKey(CustomUserAccountModel, related_name='comment_likes', on_delete=models.CASCADE)

	class Meta:
		unique_together = ('comment_link', 'user')






