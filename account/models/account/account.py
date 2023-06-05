from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from account.models.account.manager import MyAccountManager


class Account(AbstractBaseUser):

	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)

	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'   # This with login with email
	REQUIRED_FIELDS = []  # other than email

	objects= MyAccountManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True
