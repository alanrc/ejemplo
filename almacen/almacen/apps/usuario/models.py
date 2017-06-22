from django.db import models
from django.conf import settings
#from django.contrib.auth.models import User

#class Perfil(models.Model):
	#usuario = models.OneToOneField(User)


class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	fotografia = models.ImageField(upload_to='User', blank=True,null=True)
