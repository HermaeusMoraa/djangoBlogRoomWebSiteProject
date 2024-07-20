from django.urls import path
from .views import ThreadDetailView, add_comment, thread_create_view




urlpatterns = [
	# Thread
	path('thread/new/', thread_create_view, name='thread-create'),
	path('thread/<int:pk>/detail/', ThreadDetailView.as_view(), name='thread-detail'),

	# Comment
	path('thread/<int:pk>/detail/new/comment', add_comment, name='add-comment'),
]


