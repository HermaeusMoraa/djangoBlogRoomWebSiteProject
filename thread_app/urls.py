from django.urls import path
from .views import ThreadDetailView, add_comment, thread_create_view, ThreadUpdateView, ThreadDeleteView, CommentUpdateView, thread_image_create_view




urlpatterns = [
	# Thread
	path('thread/new/', thread_create_view, name='thread-create'),
	path('thread/new/image/', thread_image_create_view, name='thread-image-create'),
	path('thread/<int:pk>/detail/', ThreadDetailView.as_view(), name='thread-detail'),
	path('thread/<int:pk>/update/', ThreadUpdateView.as_view(), name='thread-update'),
	path('thread/<int:pk>/confirm/delete', ThreadDeleteView.as_view(), name='thread-delete'),

	# Comment
	path('thread/<int:pk>/detail/new/comment', add_comment, name='add-comment'),
	path('thread/<int:pk>/detail/new/comment/update/', CommentUpdateView.as_view(), name='update-comment')
]


