from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^inicio/$', home_view, name='vista_admin'),
	url(r'^help/$', help_view, name='ayuda'),

	url(r'^$',login_view),
	url(r'^logout/$',logout_view, name="cerrar_sesion"),

	url(r'^register/$', register_user, name="registrar_usuario"),

]


