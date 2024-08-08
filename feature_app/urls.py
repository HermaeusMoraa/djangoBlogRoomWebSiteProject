from django.urls import path
from .views import toggle_comment_like, toggle_thread_like, toggle_save_thread



urlpatterns = [
	path('thread/<int:pk>/detail/like/', toggle_thread_like, name='toggle-thread-like'),
	path('thread/<int:pk>/detail/commlike/', toggle_comment_like, name='toggle-comment-like'),
	path('thread/<int:pk>/detail/save/', toggle_save_thread, name='toggle-save-thread'),

]