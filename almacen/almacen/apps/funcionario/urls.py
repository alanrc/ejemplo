from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [

	url(r'^new/funcionario/$', add_funcionario, name='registrar_funcionario'),
	url(r'^funcionario/$', login_required(list_funcionario.as_view()), name='lista_funcionario'),
	url(r'^edit/funcionario/(?P<pk>\d+)/$', login_required(edit_funcionario.as_view()), name='modificar_funcionario'),
	url(r'^delete/funcionario/(?P<pk>\d+)/$', login_required(delete_funcionario.as_view()), name='eliminar_funcionario'),
	url(r'^detail/funcionario/(?P<pk>\d+)/$', login_required(detail_funcionario.as_view()), name='detalle_funcionario'),

	url(r'^search/funcionario/$', bus_fun, name='buscar_funcionario'),
	url(r'^buscar/funcionario/$', res_fun, name='resultados_funcionario'),



	#-------   unidad    --------
	url(r'^new/departamento/$', add_departamento, name='registrar_departamento'),
	url(r'^departamento/$', login_required(list_departamento.as_view()), name='lista_departamento'),
	url(r'^edit/departamento/(?P<pk>\d+)/$', login_required(edit_departamento.as_view()), name='modificar_departamento'),
	url(r'^delete/departamento/(?P<pk>\d+)/$', login_required(delete_departamento.as_view()), name='eliminar_departamento'),


	#   ////////////////  PDF   ///////////////
	url(r'^pdf/funcionario/$', generar_pdf.as_view(), name='lista_funcionario_pdf'),

]

