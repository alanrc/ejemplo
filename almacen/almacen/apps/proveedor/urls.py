from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from almacen.apps.proveedor.views import *

urlpatterns = [
	url(r'^add/proveedor/$', proveedor_add, name='registrar_proveedor'),
	url(r'^proveedor/$', login_required(proveedor_list.as_view()), name='lista_proveedor'),
	url(r'^edit/proveedor/(?P<id_prov>\d+)/$',proveedor_edit, name='editar_proveedor'),
	url(r'^delete/proveedor/(?P<id_prov>\d+)/$',proveedor_delete, name='eliminar_proveedor'),
	url(r'^detall/proveedor/(?P<id_prov>.*)/$',proveedor_detall, name='detalle_proveedor'),

	url(r'^kardex/proveedor/(?P<id_prov>\d+)$',crear_kardex, name='kardex_proveedor'),

	url(r'^search/proveedor/$', bus_prov, name='buscar_proveedor'),
	url(r'^buscar/proveedor/$', res_prov, name='resultados_proveedor'),
]