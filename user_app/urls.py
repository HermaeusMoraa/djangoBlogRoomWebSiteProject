from django.urls import path
from .views import *



urlpatterns = [
	# User login/ logout urls
	path('signup/', SignUpView.as_view(), name='signup'),
	path('dashboard/', DashboardView.as_view(), name='dashboard'),
	path('login/', CustomLoginView.as_view(), name='login'),
	path('logout/', CustomLogoutView.as_view(), name='logout'),

]