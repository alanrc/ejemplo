from django import forms
from django.core.exceptions import ValidationError
from .models import *
import datetime


class FormMarca(forms.ModelForm):
	class Meta:
		model = Marca
		fields = ['nombre','descripcion',]
		labels = {'nombre':'Nombre :', 'descripcion':'Descripcion :',}
		widgets = {'nombre':forms.TextInput(attrs = {'class':'form-control','autofocus':'true'}),'descripcion':forms.Textarea(attrs = {'class':'form-control dimension'}),	}
	'''def clean(self, *args, **kwargs):
		cleaned_data = super(FormMarca, self).clean(*args, **kwargs)
		nombre = cleaned_data.get('nombre', None)
		if nombre is not None:
			if nombre == 'alain':
				self.add_error('nombre', '"alain" no es un nombre permitido')'''

	'''def clean_nombre(self):
		num = self.cleaned_data
		nombre = num.get('nombre')
		if len(nombre)<2:
			raise forms.ValidationError("Debe ser mayor a 2 caracteres")
		return nombre'''

class FormCategoria(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = ['nombre','descripcion',]
		labels = {'nombre':'Nombre :', 'descripcion':'Descripcion :',}
		widgets = {'nombre':forms.TextInput(attrs = {'class':'form-control','autofocus':'true'}),'descripcion':forms.Textarea(attrs = {'class':'form-control dimension'}),	}

	'''def clean_nombre(self):
		num = self.cleaned_data
		nombre = num.get('nombre')
		if len(nombre)<=5:
			raise forms.ValidationError("Debe ser mayor a 5 caracteres")
		return nombre'''

class FormUnidadMedida(forms.ModelForm):
	class Meta:
		model = UnidadMedida
		fields = ['nombre','descripcion',]
		labels = {'nombre':'Nombre :', 'descripcion':'Descripcion :',}
		widgets = {'nombre':forms.TextInput(attrs = {'class':'form-control','autofocus':'true'}),'descripcion':forms.Textarea(attrs = {'class':'form-control dimension'}),	}
	'''def clean_nombre(self):
		num = self.cleaned_data
		nombre = num.get('nombre')
		if len(nombre)<5:
			raise forms.ValidationError("Debe ser mayor a 5 caracteres")
		return nombre'''

class FormAlmacen(forms.ModelForm):
	class Meta:
		model = Almacen
		fields = ['nombre','descripcion',]
		labels = {'nombre':'Nombre :', 'descripcion':'Descripcion :',}
		widgets = {'nombre':forms.TextInput(attrs = {'class':'form-control','autofocus':'true'}),'descripcion':forms.Textarea(attrs = {'class':'form-control dimension'}),	}
	'''def clean_nombre(self):
		num = self.cleaned_data
		nombre = num.get('nombre')
		if len(nombre)<5:
			raise forms.ValidationError("Debe ser mayor a 5 caracteres")
		return nombre'''


class FormMaterial(forms.ModelForm):
	class Meta:
		model = Material
		exclude = ['stock_actual']
		fields = ['nombre','marca','categoria','unidad_medida','almacen','proveedor',]
		labels = {'nombre' : 'Nombre :', 'marca' : 'Marca :', 'categoria' : 'Categoria :','unidad_medida' : 'Unidad Medida :','almacen' : 'Almacen :','proveedor' : 'Proveedor (a) :',}
		widgets = {
		'nombre' : forms.TextInput(attrs = {'class':'form-control','autofocus':'true'}),
		'marca' : forms.Select(attrs = {'class':'form-control'}),
		'categoria' : forms.Select(attrs = {'class':'form-control'}),
		'unidad_medida' : forms.Select(attrs = {'class':'form-control'}),
		'almacen' : forms.Select(attrs = {'class':'form-control'}),
		'proveedor' : forms.Select(attrs = {'class':'form-control'}),}




class FormMaterialIngreso(forms.ModelForm):
	class Meta:
		model = Ingreso
		exclude = ['material','precio_t']
		fields = ['cantidad', 'precio_u','num_factura',  'serie', 'codigo', 'objeto', 'observacion', 'funcionario',]
		labels = {'cantidad':'Cantidad :', 'precio_u':'Precio Unitario :', 'num_factura':'N° de Factura :',  'serie':'Serie :', 'codigo':'Codigo', 'objeto':'Obj. de lo Solicitado :', 'observacion':'Observacion :', 'funcionario':'Solicitado por :'}
		widgets = {
		'cantidad' : forms.TextInput(attrs = {'class':'form-control','autofocus':'true'}),
		'precio_u' : forms.TextInput(attrs = {'class':'form-control'}),
		'num_factura' : forms.TextInput(attrs = {'class':'form-control'}),

		'serie' : forms.TextInput(attrs = {'class':'form-control'}),
		'codigo' : forms.TextInput(attrs = {'class':'form-control'}),
		'objeto' : forms.Textarea(attrs = {'class':'form-control dimension'}),
		'observacion' : forms.Textarea(attrs = {'class':'form-control dimension'}),

		'funcionario' : forms.Select(attrs = {'class':'form-control'}),

		}



class FormMaterialSalida(forms.ModelForm):
	class Meta:
		model = Salida
		exclude =['material', 'ingreso',]
		fields = ['cantidad', 'objeto', 'observacion', 'funcionario',]
		labels = {'cantidad':'Cantidad :', 'objeto':'Obj. de lo Solicitado :', 'observacion':'Observacion :', 'funcionario':'Solicitado por :',}
		widgets = {
		'cantidad' : forms.TextInput(attrs = {'class':'form-control','autofocus':'true'}),
		'objeto' : forms.Textarea(attrs = {'class':'form-control dimension'}),
		'observacion' : forms.Textarea(attrs = {'class':'form-control dimension'}),
		'funcionario' : forms.Select(attrs = {'class':'form-control'}),
		}



class RangoForm (forms.Form):
	fecha_i = forms.DateField(widget = forms.TextInput(attrs={'class':'form-control', 'id':'Fecha_i', 'data-date-format':'dd/mm/yyyy'}))
	fecha_f = forms.DateField(widget = forms.TextInput(attrs={'class':'form-control', 'id':'Fecha_f', 'data-date-format':'dd/mm/yyyy'}))

	def clean_fecha_i(self):
		today = datetime.datetime.now()
		data = self.cleaned_data['fecha_i']
		if data.strftime('%d/%m/%Y') > today.strftime('%d/%m/%Y'):
			raise forms.ValidationError('No puede selecionar una fecha mayor a la fecha actual')
		return data

	def clean_fecha_f(self):
		today = datetime.datetime.now ()
		data = self.cleaned_data['fecha_f']
		if data.strftime('%d/%m/%Y') > today.strftime('%d/%m/%Y'):
			raise forms.ValidationError('No puede selecionar una fecha mayor a la fecha actual')
		return data


