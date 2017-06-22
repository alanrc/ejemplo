#encoding:utf-8
# -*- coding: cp1252 -*-
#import json
#import os
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse_lazy
from django.views.generic import View, ListView, UpdateView, DeleteView, DetailView

from pure_pagination.mixins import PaginationMixin

from .forms import FormFuncionario, FormDepartamento
from .models import Funcionario, Departamento

from almacen.apps.funcionario.utils import render_to_pdf
from datetime import *

from django.db.models import Q



@login_required(login_url = '/')
def add_funcionario(request):
	if request.method == 'POST':
		form = FormFuncionario(request.POST or None, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, "Su registro fue exitosamente. ")
			return HttpResponseRedirect('/funcionario/')
	else:
		form = FormFuncionario()
	ctx =  {'form':form}
	return render(request, 'funcionario/new_funcionario.html', ctx)

class list_funcionario(PaginationMixin, ListView):
	template_name = 'funcionario/list_funcionario.html'
	model = Funcionario
	paginate_by = 8

class edit_funcionario(UpdateView):
	model = Funcionario
	form_class = FormFuncionario
	template_name = 'funcionario/update_funcionario.html'
	success_url = reverse_lazy('lista_funcionario')

class delete_funcionario(DeleteView):
	model = Funcionario
	template_name = 'funcionario/delete_funcionario.html'
	success_url = reverse_lazy('lista_funcionario')

class detail_funcionario(DetailView):
	model = Funcionario
	template_name = 'funcionario/detail_funcionario.html'
	context_object_name = 'func'

@login_required(login_url = '/')
def bus_fun(request):
	return render(request, 'funcionario/funcionario_search.html')

@login_required(login_url = '/')
def res_fun(request):
	if request.method=="POST":
		key=request.POST["buscar"]
		resultados=Funcionario.objects.filter(Q(ci__icontains=key)|Q(nombre__icontains=key)|Q(apellidos__icontains=key))
		ctx = {"resultado":resultados}
		return render(request, "funcionario/resultados.html", ctx)
	else:
		return render(request, "funcionario/resultados.html")


#   ----------     unidad         ----------
@login_required(login_url = '/')
def add_departamento(request):
	if request.method == 'POST':
		form = FormDepartamento(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Su registro fue exitosamente. ')
			return HttpResponseRedirect('/departamento/')
	else:
		form = FormDepartamento()
	ctx = {'form':form}
	return render(request, 'departamento/new_unidad.html', ctx)

class list_departamento(PaginationMixin, ListView):
	template_name = 'departamento/lista_departamento.html'
	model = Departamento
	paginate_by = 8

class edit_departamento(UpdateView):
	model = Departamento
	form_class = FormDepartamento
	template_name = 'departamento/update_unidad.html'
	success_url = reverse_lazy('lista_departamento')

class delete_departamento(DeleteView):
	model = Departamento
	template_name = 'departamento/delete_unidad.html'
	success_url = reverse_lazy('lista_departamento')
























# /////////////   PDF   /////////////////////////

class generar_pdf(View):
	def get(self, request, *args, **kwargs):
		hora = datetime.today()
		fun = Funcionario.objects.all()
		context = {'fun':fun, 'hora':hora}
		pdf = render_to_pdf('funcionario/reporte_lista.html',context)
		if pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = "pdf_funcionario-%s.pdf" %("EMAP")
			content = "inline; filename='%s'" %(filename)
			download = request.GET.get("download")
			if download:
				content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
		return HttpResponse('no funciona')