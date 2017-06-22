#encoding:utf-8
# -*- coding: cp1252 -*-
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required


# from .forms import *
# from .models import *

@login_required(login_url = '/')
def home_view(request):
	return render(request, 'home/home.html')

#----   help   ------
@login_required(login_url = '/')
def help_view(request):
	return render(request, 'home/ayuda.html')


def register_user(request):
	return render(request, 'usuario/registro_user.html')



def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid:
			usuario = request.POST['username']
			contrasenia = request.POST['password']
			acceso = authenticate(username=usuario,password=contrasenia)
			if acceso is not None:
				if acceso.is_active:
					login(request,acceso)
					if request.user.is_staff:
						return HttpResponseRedirect('/admin/')
					else:
						messages.success(request, 'Bienvenido ')
					return HttpResponseRedirect('/inicio/')
				else:
					login(request,acceso)
					return HttpResponseRedirect('/user/active/')
			else:
				messages.success(request, "El nombre de usuario o la contraseña son incorrectos.")
				return HttpResponseRedirect('/')
				#return render(request, 'usuario/error.html')
	else:
		form = AuthenticationForm()
	ctx = {'form':form}
	return render(request, 'usuario/login.html', ctx)

#----- logout -----
@login_required(login_url = '/')
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
