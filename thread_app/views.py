from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

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



class ThreadUpdateView(LoginRequiredMixin, UpdateView):
	model = ThreadModel
	form_class = ThreadForm
	template_name = 'thread_template/thread_update.html'
	context_object_name = 'thread_update'

	def get_queryset(self):
		return self.model.objects.filter(creator=self.request.user)

	def form_valid(self, form):
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()



class ThreadDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = ThreadModel
	template_name = 'thread_template/thread_confirm_delete.html'
	success_url = reverse_lazy('home-page')
	context_object_name = 'thread_delete'

	def test_func(self):
		thread = self.get_object()
		return self.request.user == thread.creator

	def handle_no_permission(self):
		if not self.request.user.is_authenticated:
			return redirect_to_login(self.request.get_full_path())
		else:
			return HttpResponseForbidden('You are not allowed to delete this post')



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




class CommentUpdateView(LoginRequiredMixin, View):
	template_name = 'comment_template/comment_update.html'
	login_url = 'login'

	def get(self, request, pk, *args, **kwargs):
		comment = get_object_or_404(CommentModel, pk=pk, commentator=request.user)
		form = CommentForm(instance=comment)
		return render(request, self.template_name, {'form':form})

	def post(self, request, pk, *args, **kwargs):
		comment = get_object_or_404(CommentModel, pk=pk, commentator=request.user)
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			form.save()
			return redirect('thread-detail', pk=comment.thread_link.pk)
		return render(request, self.template_name, {'form': form})















