from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from almacen.apps.material.views import *

urlpatterns = [
	#  ------     marca    -------
	url(r'^add/marca/$', marca_add, name='agregar_marca'),
	url(r'^marca/$', login_required(marca_list.as_view()), name='lista_marca'),
	url(r'^delete/marca/(?P<id_mar>\d+)/$', marca_delete, name='eliminar_marca'),
	url(r'^edit/marca/(?P<id_mar>\d+)/$', marca_edit, name='editar_marca'),

	#  -----  categoria   ------
	url(r'^add/categoria/$', categoria_add, name='agregar_categoria'),
	url(r'^categoria/$', login_required(categoria_list.as_view()), name='lista_categoria'),
	url(r'^delete/categoria/(?P<id_cat>\d+)/$', categoria_delete, name='eliminar_categoria'),
	url(r'^edit/categoria/(?P<id_cat>\d+)/$', categoria_edit, name='editar_categoria'),

	#  ---   unidad de medida   ------
	url(r'^add/unidad/$', unidad_add, name='agregar_unidad'),
	url(r'^u_medida/$', login_required(unidad_list.as_view()), name='lista_u_medida'),
	url(r'^delete/unidad/(?P<id_unid>\d+)/$', unidad_delete, name='eliminar_unidad'),
	url(r'^edit/unidad/(?P<id_unid>\d+)/$', unidad_edit, name='editar_unidad'),

	#   ---  almacen    -----
	url(r'^add/almacen$', almacen_add, name='agregar_almacen'),
	url(r'^almacen/$', almacen_list, name='lista_almacen'),
	url(r'^delete/almacen/(?P<id_alm>\d+)/$', almacen_delete, name='eliminar_almacen'),
	url(r'^edit/almacen/(?P<id_alm>\d+)/$', almacen_edit, name='editar_almacen'),

	#  --------   material    -------------
	url(r'^add/material/$', material_add, name='registrar_material'),
	url(r'^material/$', login_required(material_list.as_view()), name='lista_material'),
	url(r'^edit/material/(?P<id_mat>\d+)/$',material_edit, name='editar_material'),
	url(r'^delete/material/(?P<id_mat>\d+)/$',material_delete, name='eliminar_material'),
	url(r'^detall/material/(?P<id_mat>.*)/$',material_detall, name='detalle_material'),
	url(r'^search/material/$', bus_mat, name='buscar_material'),
	url(r'^buscar/material/$', res_mat, name='resultados_material'),

	#-----------  ingreso material ------------
	url(r'^ingreso/material/(?P<id_prod>\d+)/$',material_ingreso, name='ingreso_material'),
	url(r'^ingresos/$', login_required(mat_ing_list.as_view()), name='lista_mat_ingreso'),
	url(r'^detalle/ingreso/(?P<id_ing>\d+)/$',mat_ing_detall, name='detalle_mat_ingreso'),

	url(r'^search/ingreso/$', bus_ing, name='buscar_ingreso'),
	url(r'^buscar/ingreso/$', res_ing, name='resultados_ingreso'),

	# -----------   salida material    ---------
	url(r'^salida/material/(?P<id_prod>\d+)/$',material_salida, name='salida_material'),
	url(r'^salidas/$', login_required(mat_sal_list.as_view()), name='lista_mat_salida'),


	url(r'^detalle/salida/(?P<id_sal>\d+)/$',mat_sal_detall, name='detalle_mat_salida'),

	url(r'^search/salida/$', bus_sal, name='buscar_salida'),
	url(r'^buscar/salida/$', res_sal, name='resultados_salida'),


	#   -----  reportes -----
	url(r'^reporte/$', reporte_fecha, name='reporte_fecha'),



	url(r'^reporte/material/$', reporte_material, name='reporte_material'),
	url(r'^reporte/resultado/$', resultado_mat, name='resultado_material_todo'),
	# url(r'^detalle/(?P<id_prod>\d+)/$', kardex_material_to, name='detalle_material_todo'),


	#  //////////////////////////               PDF                 ///////////////////////////////////////

	#  /////////////////        KARDEX            /////////////////

	#--------------------- kardex-ingreso  --------------
	url(r'^kardex/ingreso/(?P<id_ing>\d+)/$', kardex_ingreso, name='kardex_ingreso'),

	#--------------------- kardex-salida  --------------
	url(r'^kardex/salida/(?P<id_salida>\d+)/$', crear_kardex, name='crear_kardex_salida'),



	#  //////////////////         REPORTES           //////////////////

	#  ---------------------- reporte por ingresos   --------------------------------
	url (r'ingresos/generar_reporte/$', reporte_lista_ingresos, name = 'generar_reporte_lista_ingresos'),

	#  ----------------- reporte por salidas   --------------------------------
	url (r'salidas/generar_reporte/$', reporte_lista_salida, name = 'generar_reporte_lista_salidas'),




	url(r'^pdf/salida/(?P<pk>\d+)/$', generate_pdf.as_view(), name='kardex_salida'),

	#  ------------------    kardex fisico por material   -------------------------
	#url(r'^pdf/kardex/material/$', generar_material_pdf.as_view(), name='kardex_por_material'),
]

	# url(r'^pdf/ingreso/$', generatepdf.as_view(), name='kardex_ingreso'),
	#url(r'^pdf/salida/$', generate_pdf.as_view(), name='kardex_salida'),