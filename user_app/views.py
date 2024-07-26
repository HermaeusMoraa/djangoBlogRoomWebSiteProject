from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from thread_app.models import ThreadModel
from .forms import CustomUserCreationForm, LoginForm, CustomUserAccountChangeForm, CustomUserProfileChangeForm
from django.contrib.auth import login, authenticate, logout

from .models import CustomUserAccountModel


### USER LOGIN LOGIC ###

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


### USER DASHBOARD LOGIC ###

class DashboardView(LoginRequiredMixin, TemplateView):
	template_name = 'user_template/user_dashboard.html'
	login_url = 'login'

	def dispatch(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect('login')
		return super().dispatch(request, *args, **kwargs)




class UserThreadView(LoginRequiredMixin, ListView):
	model = ThreadModel
	template_name = 'user_template/user_threads.html'
	context_object_name = 'threads_user'
	login_url = 'login'

	def get_queryset(self):
		return ThreadModel.objects.filter(creator=self.request.user)




class UserAccountView(LoginRequiredMixin, View):
	template_name = 'user_template/user_account.html'
	login_url = 'login'

	def get(self, request, *args, **kwargs):
		form = CustomUserAccountChangeForm(instance=request.user)
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = CustomUserAccountChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('user-account')
		return render(request, self.template_name, {'form': form})



class UserProfileView(LoginRequiredMixin, View):

	template_name = 'user_template/user_profile.html'
	login_url = 'login'

	def get(self, request, *args, **kwargs):
		form = CustomUserProfileChangeForm(instance=request.user)
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = CustomUserProfileChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('user-profile')
		return render(request, self.template_name, {'form': form})


