from django.urls import path
from .views import toggle_comment_like, toggle_thread_like



urlpatterns = [
	path('thread/<int:pk>/detail/like/', toggle_thread_like, name='toggle-thread-like'),
	path('thread/<int:pk>/detail/commlike/', toggle_comment_like, name='toggle-comment-like'),

]