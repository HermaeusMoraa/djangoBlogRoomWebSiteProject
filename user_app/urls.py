from django.urls import path
from .views import *



urlpatterns = [
	# User login/ logout urls
	path('dashboard/', DashboardView.as_view(), name='dashboard'),
	path('dashboard/myaccount/', UserAccountView.as_view(), name='user-account'),
	path('dashboard/myprofile/', UserProfileView.as_view(), name='user-profile'),
	path('dashboard/myposts/', UserThreadView.as_view(), name='user-threads'),


	path('signup/', SignUpView.as_view(), name='signup'),
	path('login/', CustomLoginView.as_view(), name='login'),
	path('logout/', CustomLogoutView.as_view(), name='logout'),

]
