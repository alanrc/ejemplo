from django.db import models
#from almacen.apps.material.models import Ingreso, Salida

class Departamento (models.Model):
	nombre = models.CharField(max_length=50)

	class Meta:
		verbose_name='Departamento'
		verbose_name_plural='Departamentos'
		ordering = ['nombre']

	def __str__(self):
		return self.nombre


CARGO  = (
			('', 'Selecione    Cargo '),
			('Auditor (a)', 'Auditor (a)'),
			('Cotizador (a)', 'Cotizador (a)'),
			('Contador (a)', 'Contador (a)'),
			('Enc. Almacenes', 'Enc. Almacenes'),
			('Enc. Area Tecnica', 'Enc. Area Tecnica'),
			('Enc. Bienes', 'Enc. Bienes'),
			('Enc. R. Humanos ', 'Enc. R. Humanos '),
			('Enc. Tesoreria', 'Enc. Tesoreria'),
			('Enc. Soldaduria', 'Enc. Soldaduria'),
			('Gerente General', 'Gerente General'),
			('Ing. de Sistemas', 'Ing. de Sistemas'),
			('Mecanico', 'Mecanico'),
			('Resp. Archivos', 'Resp. Archivos'),
			('Secretaria', 'Secretaria'),
			('Supervisor', 'Supervisor'),
		)
class Funcionario (models.Model):
	ci = models.PositiveIntegerField(unique=True)
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	cargo = models.CharField(choices = CARGO, max_length=50)
	direccion = models.CharField(max_length=100)
	telefono = models.PositiveIntegerField()

	unidad = models.ForeignKey(Departamento)

	#ingreso = models.ForeignKey(Ingreso)
	#salida = models.ForeignKey(Salida)

	class Meta:
		verbose_name = "Funcionario"
		verbose_name_plural = "Funcionarios"
		ordering = ['cargo']

	def __str__(self):
		return '%s %s' % (self.nombre, self.apellidos)

		
