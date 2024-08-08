
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import CommentLikeModel, ThreadLikeModel, SavedThreadModel
from thread_app.models import CommentModel, ThreadModel


@login_required
def toggle_thread_like(request, pk):
	thread = get_object_or_404(ThreadModel, pk=pk)
	like, created = ThreadLikeModel.objects.get_or_create(thread_link=thread, user= request.user)
	if not created:
		like.delete()
		liked = False
	else:
		liked = True
	# return redirect('thread-detail', pk=pk)
	return JsonResponse({'liked': liked, 'like_count': thread.like_count()})


@login_required
def toggle_comment_like(request, pk):
	comment = get_object_or_404(CommentModel, pk=pk)
	like, created = CommentLikeModel.objects.get_or_create(comment_link= comment, user= request.user)
	if not created:
		like.delete()
		liked = False
	else:
		liked = True
	# return redirect('thread-detail', pk=pk)
	return JsonResponse({'liked': liked, 'like_count': comment.like_count()})



@login_required
def toggle_save_thread(request, pk):
	thread = get_object_or_404(ThreadModel, pk=pk)
	saved_thread, created = SavedThreadModel.objects.get_or_create(user=request.user, thread_link=thread)

	if not created:
		saved_thread.delete()
		return JsonResponse({'saved': False})

	return JsonResponse({'saved': True})







