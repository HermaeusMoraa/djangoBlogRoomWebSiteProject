from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from django.utils import timezone
from .country_list import COUNTRY_CHOICES


class CustomUserAccountModel(AbstractUser):

	gender_option = (
		('M', 'Male'),
		('F', 'Female'),
	)

	# UserAccount
	# - username
	# - email

	# UserProfile
	country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, null=True, blank=True)
	gender = models.CharField(max_length=1, choices=gender_option, null=True, blank=True)
	date_of_birth = models.DateField(null=True, blank=True)
	about = models.TextField(max_length=1000, null=True, blank=True)

	# Avatar/Bg
	# avatar = models.ImageField(upload_to='#/', null=True, blank=True)
	# background = models.ImageField(upload_to='#/', null=True, blank=True)

	# Autofilled
	joined_date = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.username


