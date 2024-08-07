
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import CommentLikeModel, ThreadLikeModel
from thread_app.models import CommentModel, ThreadModel


@login_required
def toggle_thread_like(request, pk):
	post = get_object_or_404(ThreadModel, pk=pk)
	like, created = ThreadLikeModel.objects.get_or_create(post=post, user= request.user)
	if not created:
		like.delete()
		liked = False
	else:
		liked = True
	return JsonResponse({'liked': liked, 'like_count': post.like_count()})



def toggle_comment_like(request, pk):
	comment = get_object_or_404(CommentModel, pk=pk)
	like, created = CommentLikeModel.objects.get_or_create(comment= comment, user= request.user)
	if not created:
		like.delete()
		liked = False
	else:
		liked = True
	return JsonResponse({'liked': liked, 'like_count': comment.like_count()})













