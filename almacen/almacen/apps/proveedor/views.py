#encoding:utf-8
# -*- coding: cp1252 -*-
import os
from io import BytesIO
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import ListView
from pure_pagination.mixins import PaginationMixin

import xhtml2pdf.pisa as pisa
from django import http
from django.template.loader import get_template, render_to_string
from django.template import RequestContext
import cgi

from .forms import FormProveedor
from .models import Proveedor
from django.contrib.auth.decorators import login_required
from django.db.models import Q

this_path = os.getcwd() + '/proveedor/'

@login_required(login_url = '/')
def proveedor_add(request):
	if request.method == 'POST':
		form = FormProveedor(request.POST or None, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, "Se registro con exito...")
			return HttpResponseRedirect('/proveedor/')
	else:
		form = FormProveedor()
	ctx =  {'form':form}
	return render(request, 'proveedor/proveedor_add.html', ctx)


class proveedor_list(PaginationMixin, ListView):
	template_name = 'proveedor/proveedor_list.html'
	model = Proveedor
	paginate_by = 8

@login_required(login_url = '/')
def proveedor_edit(request, id_prov):
	prov = get_object_or_404(Proveedor, id = id_prov)
	if request.method == 'GET':
		form = FormProveedor(instance = prov)
	else:
		form = FormProveedor(request.POST, request.FILES, instance = prov)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/proveedor/page/1/')
	ctx = {'form':form}
	return render(request, 'proveedor/proveedor_edit.html', ctx)

@login_required(login_url = '/')
def proveedor_delete(request, id_prov):
	prov = get_object_or_404(Proveedor, id = id_prov)
	#prov = proveedor.objects.get(id=id_prov)
	if request.method == 'POST':
		prov.delete()
		messages.success(request, "Se elimino con exito...")
		return HttpResponseRedirect('/proveedor/page/1/')
	ctx = {'prov':prov}
	return render(request, 'proveedor/proveedor_delete.html',ctx)

@login_required(login_url = '/')
def proveedor_detall(request, id_prov):
	prov = get_object_or_404(Proveedor, id = id_prov)
	#prov = proveedor.objects.get(id=id_prov)
	ctx={'proveedor':prov}
	return render(request, 'proveedor/proveedor_detall.html',ctx)

@login_required(login_url = '/')
def bus_prov(request):
	return render(request,'proveedor/proveedor_search.html')

@login_required(login_url = '/')
def res_prov(request):
	if request.method=="POST":
		key=request.POST["buscar"]
		resultados=Proveedor.objects.filter(Q(ci__icontains=key)|Q(nombre__icontains=key)|Q(apellidos__icontains=key))
		ctx = {"resultado":resultados}
		return render(request,"proveedor/resultados.html",ctx)
	else:
		return render(request,"proveedor/resultados.html")





@login_required(login_url = '/')
def crear_kardex(request, id_prov):
	prov =  get_object_or_404(Proveedor, id = id_prov)
	html = render_to_string('proveedor/kardex_proveedor.html', {'prov':prov}, context_instance = RequestContext(request))
	return generar_pdf(html)


def generar_pdf(html):
	resultado  = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), resultado)
	if not pdf.err:
		return HttpResponse(resultado.getvalue(), content_type = 'application/pdf')
	else:
		return HttpResponse("Error al generar el pdf: %s" % cgi.escape(html))
