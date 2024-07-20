from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView

from .forms import ThreadForm, CommentForm
from .models import ThreadModel, CommentModel

# Thread Logic

@login_required
def thread_create_view(request):
	if request.method == 'POST':
		form = ThreadForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.creator = request.user
			post.save()
			return redirect('home-page')
	else:
		form = ThreadForm()
	return render(request, 'thread_template/thread_create.html', {'form':form})




class ThreadDetailView(DetailView):
	model = ThreadModel
	template_name = 'thread_template/thread_detail.html'
	context_object_name = 'thread'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = CommentForm()
		context['comments'] = CommentModel.objects.filter(thread_link=self.object)
		return context





# Comment Logic
@login_required
def add_comment(request, pk):
	thread = get_object_or_404(ThreadModel, pk=pk)

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.thread_link = thread
			comment.commentator = request.user
			comment.save()
			return redirect('thread-detail', pk=thread.pk)
	else:
		form = CommentForm()
	context = {'form': form, 'thread_comment': thread}
	return render(request, 'comment_template/comment_create.html', context)








