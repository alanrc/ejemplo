from django import forms
from .models import Proveedor
from django.core.exceptions import ValidationError
#from almacen.apps.proveedor.models import Proveedor

class FormProveedor(forms.ModelForm):
	class Meta:
		model = Proveedor
		fields = ["ci","nombre","apellidos","genero","telefono","email","domicilio","empresa","photo",]
		labels = {'ci':'Cedula de Identidad :', 'nombre':'Nombres :', 'apellidos':'Apellidos :', 'genero':'Genero :', 'telefono':'Telefono :','email':'E-mail :', 'domicilio':'Direccion :', 'empresa':'Empresa:', 'photo':'Fotografia :',}
		widgets = {
		'ci' : forms.TextInput(attrs={'class':'form-control','autofocus':'true'}),
		'nombre' : forms.TextInput(attrs={'class':'form-control'}),
		'apellidos' : forms.TextInput(attrs={'class':'form-control'}),
		'genero' : forms.Select(attrs={'class':'form-control'}),
		'telefono' : forms.TextInput(attrs={'class':'form-control'}),
		'email' : forms.TextInput(attrs={'class':'form-control'}),
		'domicilio' : forms.TextInput(attrs={'class':'form-control'}),
		'empresa' : forms.TextInput(attrs={'class':'form-control'}),
		}