from django.urls import path
from .views import *



urlpatterns = [
	# User dashboard urls
	path('dashboard/', DashboardView.as_view(), name='dashboard'),
	path('dashboard/myaccount/', UserAccountView.as_view(), name='user-account'),
	path('dashboard/myprofile/', UserProfileView.as_view(), name='user-profile'),
	path('dashboard/myposts/', UserThreadView.as_view(), name='user-threads'),
	path('dashboard/mysaves', saved_threads, name='saved-threads'),

	# User login/ logout urls
	path('signup/', SignUpView.as_view(), name='signup'),
	path('login/', CustomLoginView.as_view(), name='login'),
	path('logout/', CustomLogoutView.as_view(), name='logout'),

]
