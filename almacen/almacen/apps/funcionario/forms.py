from django import forms
from .models import Funcionario, Departamento
from django.core.exceptions import ValidationError
#from almacen.apps.proveedor.models import Proveedor

class FormFuncionario(forms.ModelForm):
	class Meta:
		model = Funcionario
		fields = ["ci","nombre","apellidos","telefono","cargo","direccion", 'unidad',]
		labels = {'ci':'Cedula de Identidad :', 'nombre':'Nombre :', 'apellidos':'Apellidos :', 'telefono':'Telefono :','cargo':'Cargo :', 'direccion':'Direccion :', 'unidad':' Trabaja en la Unidad :',}
		widgets = {
		'ci' : forms.TextInput(attrs={'class':'form-control','autofocus':'true'}),
		'nombre' : forms.TextInput(attrs={'class':'form-control'}),
		'apellidos' : forms.TextInput(attrs={'class':'form-control'}),
		'telefono' : forms.TextInput(attrs={'class':'form-control'}),
		'cargo' : forms.Select(attrs={'class':'form-control'}),
		'direccion' : forms.TextInput(attrs={'class':'form-control'}),
		'unidad' : forms.Select(attrs={'class':'form-control'}),
		}

class FormDepartamento(forms.ModelForm):
	class Meta:
		model = Departamento
		fields = ["nombre",]
		labels = {'nombre':'Nombre :',}
		widgets = {'nombre' : forms.TextInput(attrs={'class':'form-control','autofocus':'true'}),}
	
	def clean_nombre(self):
		nombre = self.cleaned_data['nombre']
		if Departamento.objects.filter(nombre = nombre):
			raise forms.ValidationError( 'Ya existe esta Unidad')
		return nombre
