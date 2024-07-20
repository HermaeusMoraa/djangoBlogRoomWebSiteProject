from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import login, authenticate, logout







class SignUpView(CreateView):

	form_class = CustomUserCreationForm
	template_name = 'user_template/user_signup.html'
	success_url = reverse_lazy('dashboard')

	def form_valid(self, form):
		response = super().form_valid(form)
		user = authenticate(username=form.cleaned_data['username'],
		                    password=form.cleaned_data['password1'])
		login(self.request, user)
		return response



class DashboardView(TemplateView):
	template_name = 'user_template/user_dashboard.html'

	def dispatch(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect('login')
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		# Handle POST request here
		# For example, you might process a form submission
		# You can access POST data with request.POST
		# If you need to redirect or render a response based on POST data, do it here

		# Example of processing a form submission:
		# form = MyForm(request.POST)
		# if form.is_valid():
		#     # Process form data
		#     return redirect('some-view-name')

		# If you want to render the same template, pass any context if needed
		context = self.get_context_data(**kwargs)
		return self.render_to_response(context)



class CustomLoginView(LoginView):
	form_class = LoginForm
	template_name = 'user_template/user_login.html'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('home-page')



class CustomLogoutView(LogoutView):
	def dispatch(self, *args, **kwargs):
		logout(self.request)
		return redirect('login')














