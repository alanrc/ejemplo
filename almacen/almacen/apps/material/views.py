#encoding:utf-8
# -*- coding: cp1252 -*-
import os
from io import BytesIO, StringIO

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *

from django.views.generic import View, ListView
from pure_pagination.mixins import PaginationMixin
#from django.template.loader import get_template, 

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.template import RequestContext

from almacen.apps.material.utils import render_to_pdf
from datetime import *


import xhtml2pdf.pisa as pisa
from django import http
from django.template.loader import get_template, render_to_string
import cgi

from django.db.models import Q

#   ----   marca    -----
@login_required(login_url = '/')
def marca_add(request):
	if request.method == 'POST':
		form = FormMarca(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Su registro fue exitosamente. ')
			return HttpResponseRedirect('/marca/')
	else:
		form = FormMarca()
	ctx = {'form':form}
	return render(request, 'marca/marca_add.html', ctx)

class marca_list(PaginationMixin, ListView):
	template_name = 'marca/marca_list.html'
	model = Marca
	paginate_by = 8

@login_required(login_url = '/')
def marca_edit(request, id_mar):
	mar = get_object_or_404(Marca, id = id_mar)
	if request.method == 'GET':
		form = FormMarca(instance = mar)
	else:
		form = FormMarca(request.POST, instance = mar)
		if form.is_valid():
			form.save()
			#messages.add_message(request,messages.SUCCESS,"Los datos se modificaron con exito")
		return HttpResponseRedirect('/marca/')
	ctx = {'form':form}
	return render(request, 'marca/marca_edit.html', ctx)

@login_required(login_url = '/')
def marca_delete(request, id_mar):
	mar = get_object_or_404(Marca, id = id_mar)
	if request.method == 'POST':
		mar.delete()
		return HttpResponseRedirect('/marca/')
	ctx = {'mar':mar}
	return render(request, 'marca/marca_delete.html', ctx)

#  -----  categoria    -------

@login_required(login_url = '/')
def categoria_add(request):
	if request.method == 'POST':
		form = FormCategoria(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Su registro fue exitosamente. ')
			return HttpResponseRedirect('/categoria/')
	else:
		form = FormCategoria()
	ctx ={'form':form}
	return render(request, 'categoria/categoria_add.html', ctx)

class categoria_list(PaginationMixin, ListView):
	template_name = 'categoria/categoria_list.html'
	model = Categoria
	paginate_by = 8


@login_required(login_url = '/')
def categoria_edit(request, id_cat):
	cat = get_object_or_404(Categoria, id = id_cat)
	if request.method == 'GET':
		form = FormCategoria(instance = cat)
	else:
		form = FormCategoria(request.POST, instance = cat)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/categoria/')
	ctx = {'form':form}
	return render(request, 'categoria/categoria_edit.html', ctx)

@login_required(login_url = '/')
def categoria_delete(request, id_cat):
	cat = get_object_or_404(Categoria, id = id_cat)
	if request.method == 'POST':
		cat.delete()
		return HttpResponseRedirect('/categoria/')
	ctx = {'cat':cat}
	return render(request, 'categoria/categoria_delete.html', ctx)


#   ----  unidad de medida   ------

@login_required(login_url = '/')
def unidad_add(request):
	if request.method == 'POST':
		form = FormUnidadMedida(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Su registro fue exitosamente. ')
			return HttpResponseRedirect('/u_medida/')
	else:
		form = FormUnidadMedida()
	ctx = {'form':form}
	return render(request, 'unidad/unidad_add.html', ctx)

class unidad_list(PaginationMixin, ListView):
	template_name = 'unidad/unidad_list.html'
	model = UnidadMedida
	paginate_by = 8

@login_required(login_url = '/')
def unidad_edit(request, id_unid):
	unid = get_object_or_404(UnidadMedida, id = id_unid)
	if request.method == 'GET':
		form = FormUnidadMedida(instance = unid)
	else:
		form = FormUnidadMedida(request.POST, instance = unid)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/u_medida/')
	ctx = {'form':form}
	return render(request, 'unidad/unidad_edit.html', ctx)

@login_required(login_url = '/')
def unidad_delete(request, id_unid):
	unid = get_object_or_404(UnidadMedida, id = id_unid)
	if request.method == 'POST':
		unid.delete()
		return HttpResponseRedirect('/u_medida/')
	ctx = {'unid':unid}
	return render(request, 'unidad/unidad_delete.html', ctx)

#   -----  almacen   ------

@login_required(login_url = '/')
def almacen_add(request):
	if request.method == 'POST':
		form = FormAlmacen(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Su registro fue exitosamente. ')
			return HttpResponseRedirect('/almacen/')
	else:
		form = FormAlmacen()
	ctx = {'form':form}
	return render(request, 'almacen/almacen_add.html', ctx)

@login_required(login_url = '/')
def almacen_list(request):
	alm = Almacen.objects.all()
	ctx = {'a': alm}
	return render(request, 'almacen/almacen_list.html', ctx)

@login_required(login_url = '/')
def almacen_edit(request, id_alm):
	alm = get_object_or_404(Almacen, id = id_alm)
	if request.method == 'GET':
		form = FormAlmacen(instance = alm)
	else:
		form = FormAlmacen(request.POST, instance = alm)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/almacen/')
	ctx = {'form':form}
	return render(request, 'almacen/almacen_edit.html', ctx)

@login_required(login_url = '/')
def almacen_delete(request, id_alm):
	alm = get_object_or_404(Almacen, id = id_alm)
	if request.method == 'POST':
		alm.delete()
		return HttpResponseRedirect('/almacen/')
	ctx = {'alm':alm}
	return render(request, 'almacen/almacen_delete.html', ctx)


#  -----  producto   -----

@login_required(login_url = '/')
def material_add(request):
	if request.method == 'POST':
		form = FormMaterial(request.POST, request.FILES)
		if form.is_valid():
			p = Material(
				nombre = form.cleaned_data["nombre"],
				marca = form.cleaned_data["marca"],
				categoria = form.cleaned_data["categoria"],
				unidad_medida = form.cleaned_data["unidad_medida"],
				almacen = form.cleaned_data["almacen"],
				proveedor = form.cleaned_data["proveedor"],
				)
			p.save()
			messages.success(request, 'Su registro fue exitosamente. ')
			return HttpResponseRedirect('/material/')
	else:
		form = FormMaterial()
	ctx = {'form':form}
	return render(request, 'material/material_add.html', ctx)

class material_list(PaginationMixin, ListView):
	template_name = 'material/material_list.html'
	model = Material
	paginate_by = 8

@login_required(login_url = '/')
def material_edit(request, id_mat):
	prod = get_object_or_404(Material, id = id_mat)
	if request.method == 'GET':
		form = FormMaterial(instance = prod )
	else:
		form = FormMaterial(request.POST, request.FILES, instance = prod)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/material/')
	ctx = {'form':form}
	return render(request, 'material/material_edit.html', ctx)

@login_required(login_url = '/')
def material_delete(request, id_mat):
	prod = get_object_or_404(Material, id = id_mat)
	#prod = Producto.objects.get(id=id_prod)
	if request.method == 'POST':
		prod.delete()
		return HttpResponseRedirect('/material/')
	ctx = {'prod':prod}
	return render(request, 'material/material_delete.html', ctx)

@login_required(login_url = '/')
def material_detall(request, id_mat):
	prod = get_object_or_404(Material, id = id_mat)
	ctx = {'producto':prod}
	return render(request, 'material/material_detall.html', ctx)

@login_required(login_url = '/')
def bus_mat(request):
	return render(request, 'material/material_search.html')

@login_required(login_url = '/')
def res_mat(request):
	if request.method=="POST":
		key=request.POST["buscar"]
		resultados=Material.objects.filter(Q(nombre__icontains=key))
		ctx = {"resultado":resultados}
		return render(request, "material/resultados.html", ctx)
	else:
		return render(request, "material/resultados.html")

#----- material ingreso -------

@login_required(login_url = '/')
def material_ingreso(request, id_prod):
	prod = get_object_or_404(Material, id = id_prod)
	if request.method == 'GET':
		form = FormMaterialIngreso(instance = prod )
	else:
		form = FormMaterialIngreso(request.POST)
		if form.is_valid():
			cantidad = int(request.POST['cantidad'])
			precio_u = float(request.POST['precio_u'])
			precio_total = float(cantidad * precio_u)
			prod.stock_actual = prod.stock_actual + cantidad
			prod.save()
			ingreso = form.save(commit=False)
			ingreso.material = prod
			ingreso.precio_t = precio_total
			ingreso.save()
			#return HttpResponse(precio_total)
			messages.success(request, 'Su registro de ingreso fue exitosamente. ')
			return HttpResponseRedirect('/ingresos/')
	ctx = {'form':form,'prod':prod}
	return render(request, 'ingreso/ingreso_add.html', ctx)

class mat_ing_list(PaginationMixin, ListView):
	template_name = 'ingreso/ingreso_list.html'
	model = Ingreso
	paginate_by = 8

@login_required(login_url = '/')
def mat_ing_detall(request, id_ing):
	ing = get_object_or_404(Ingreso, id = id_ing)
	ctx = {'ing':ing}
	return render(request, 'ingreso/ingreso_detall.html', ctx)

@login_required(login_url = '/')
def bus_ing(request):
	return render(request, 'ingreso/ingreso_search.html')

@login_required(login_url = '/')
def res_ing(request):
	if request.method=="POST":
		key=request.POST["buscar"]
		resultados=Ingreso.objects.filter(Q(num_factura__icontains=key))
		ctx = {"resultado":resultados}
		return render(request, "ingreso/resultados.html", ctx)
	else:
		return render(request, "ingreso/resultados.html")

# ---------  material salida ------

@login_required(login_url = '/')
def material_salida(request, id_prod):
	prod = get_object_or_404(Material, id = id_prod)
	if request.method == 'GET':
		form = FormMaterialSalida(instance = prod )
	else:
		form = FormMaterialSalida(request.POST)
		if form.is_valid():
			cantidad = int(request.POST['cantidad'])
			stock = prod.stock_actual
			if cantidad <= stock:
				prod.stock_actual = prod.stock_actual - cantidad
				prod.save()
				salida = form.save(commit=False)
				salida.material = prod
				salida.save()
				messages.success(request, 'Su registro de salida fue exitosamente. ')
			else:
				return HttpResponse("Error la cantidad es mayor al stock")
			return HttpResponseRedirect('/salidas/')
	ctx = {'form':form, 'prod':prod}
	return render(request, 'salida/salida_add.html', ctx)

class mat_sal_list(PaginationMixin, ListView):
	template_name = 'salida/salida_list.html'
	model = Salida
	paginate_by = 8



@login_required(login_url = '/')
def mat_sal_detall(request, id_sal):
	sal = get_object_or_404(Salida, id = id_sal)
	ctx = {'sal':sal}
	return render(request, 'salida/salida_detalle.html', ctx)

@login_required(login_url = '/')
def bus_sal(request):
	return render(request, 'salida/salida_search.html')

@login_required(login_url = '/')
def res_sal(request):
	if request.method=="POST":
		key=request.POST["buscar"]
		resultados=Salida.objects.filter(Q(cantidad__icontains=key))
		ctx = {"resultado":resultados}
		return render(request, "salida/resultados.html", ctx)
	else:
		return render(request, "salida/resultados.html")



# ------ reporte por fecha -----
def reporte_fecha(request):
	return render(request, 'reportes/reporte_fecha.html')

# -------         reporte por material   --------------

@login_required(login_url = '/')
def reporte_material(request):
	return render(request, 'reportes/reporte_material.html')

@login_required(login_url = '/')
def resultado_mat(request):
	if request.method=="POST":
		key=request.POST["buscar"]
		resultados=Material.objects.filter(Q(nombre__icontains=key))
		ctx = {"resultado":resultados}
		return render(request, "kardex/resultados.html", ctx)
	else:
		return render(request, "kardex/resultados.html")


#   ///////////////////////////      PDF     //////////////////////////////
#   **************   KARDEX    ***************
# -----------     kardex-ingreso     ------------
@login_required(login_url = '/')
def kardex_ingreso(request, id_ing):
	ing = get_object_or_404(Ingreso, id = id_ing)
	ctx =  {'ing':ing}
	return render_to_pdf('pdf/kardex_ingreso.html', ctx)

# -----------     kardex-salida     ------------
@login_required(login_url = '/')
def crear_kardex(request, id_salida):
	salida =  get_object_or_404(Salida, id = id_salida)
	html = render_to_string('pdf/kardex_salida.html', {'salida':salida}, context_instance = RequestContext(request))
	return generar_pdf(html)


def generar_pdf(html):
	resultado  = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), resultado)
	if not pdf.err:
		return HttpResponse(resultado.getvalue(), content_type = 'application/pdf')
	else:
		return HttpResponse("Error al generar el pdf: %s" % cgi.escape(html))

#---------  kardex por material ------------------


#  /////////////////////////     REPORTES     /////////////////////////////


def write_pdf(template_src, context_dict):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return http.HttpResponse(result.getvalue(), content_type='application/pdf')
	return http.HttpResponse('Ocurrio un error al generar el reporte %s' % cgi.escape(html))

# ----------------------   reportes por ingresos    -------------------------
@login_required(login_url = '/')
def reporte_lista_ingresos(request):
	hora = datetime.today()

	if request.method == "POST":
		formbusqueda = RangoForm(request.POST)
		if formbusqueda.is_valid():
			fecha_in = formbusqueda.cleaned_data['fecha_i']
			fecha_fi = formbusqueda.cleaned_data['fecha_f']
			rango = Ingreso.objects.filter(fecha_i__gte=(fecha_in), fecha_i__lte=(fecha_fi)).order_by('fecha_i')
			# rango = Ingreso.objects.filter(fecha__range=(fecha_in, fecha_fi))

			total = 0
			for exp in rango:
				total = ((exp.precio_t) + (total))

			return write_pdf ('ingreso/reporte_lista_ingreso.html',{'rango' : rango, 'total':total, 'hora':hora})
		else:
			error = "Hay un error en las fechas proporcionadas"
			return render_to_response('reportes/reporte_ingresos.html', {'error': error}, context_instance=RequestContext(request))
	return render_to_response('reportes/reporte_ingresos.html', {'rangoform': RangoForm()}, context_instance=RequestContext(request))

# -------------------- reportes por salidas    --------------------------------
@login_required(login_url = '/')
def reporte_lista_salida(request):
	hora = datetime.today()

	if request.method == "POST":
		formbusqe = RangoForm(request.POST)
		if formbusqe.is_valid():
			fecha_ini = formbusqe.cleaned_data['fecha_i']
			fecha_fin = formbusqe.cleaned_data['fecha_f']
			rango_f = Salida.objects.filter(fecha__gte=(fecha_ini), fecha__lte=(fecha_fin)).order_by('fecha')
			return write_pdf('salida/reporte_lista_salida.html', {'rango_f':rango_f, 'hora':hora})
		else:
			error = "Hay un error en las fechas proporcionadas"
			return render_to_response('reportes/reportes_salida.html', {'error':error}, context_instance=RequestContext(request))
	return render_to_response('reportes/reportes_salida.html', {'rangoform':RangoForm()}, context_instance=RequestContext(request))

















































#---- reporte de kardex ingreso  ------------------
class generatepdf(View):
	def get(self, request, *args, **kwargs):
		template = get_template('pdf/reporte_ingreso.html')
		mar = Marca.objects.all()
		context = {'mar':mar}
		html = template.render(context)
		pdf = render_to_pdf('pdf/reporte_ingreso.html',context)
		if pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = "kardex_ingreso%s.pdf" %("EMAP")
			content = "inline; filename='%s'" %(filename)
			download = request.GET.get("download")
			if download:
				content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
		return HttpResponse('no funciona')


#---  reporte de kardex salida  ------------------
class generate_pdf(View):
	def get_context_data(self, request, *args, **kwargs):
		#template = get_template('pdf/kardex_salida.html')
		context = super(Salida, self).get_context_data(**kwargs)
		context ['salida'] = Salida.objects.filter(material=self.kwargs['pk'])
		#html = template.render(context)
		pdf = render_to_pdf('pdf/kardex_salida.html',context)
		#return HttpResponse(pdf, content_type = "application/pdf")
		if pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = "kardex_salida%s.pdf" %("EMAP")
			content = "inline; filename='%s'" %(filename)
			download = request.GET.get_context_data("download")
			if download:
				content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
		return HttpResponse('no funciona')





#  ---------------------------------------------------
class generar_material_pdf(View):
	def get(self, request, *args, **kwargs):
		pdf = render_to_pdf('pdf/kardex_material.html')
		if pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = "kardex-material-%s.pdf" %("EMAP")
			content = "inline; filename='%s'" %(filename)
			download = request.GET.get("download")
			if download:
				content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
		return HttpResponse('no funciona')




