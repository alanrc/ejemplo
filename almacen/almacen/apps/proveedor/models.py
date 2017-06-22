from django.db import models

genero = (('', 'Selecione Genero '),('Masculino','Masculino'),('Femenino','Femenino'),)
class Proveedor(models.Model):
	ci = models.IntegerField(unique=True)
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	genero = models.CharField(max_length=15, choices=genero)
	telefono = models.CharField(max_length=10)
	email = models.EmailField()
	domicilio = models.CharField(max_length=40)
	empresa = models.CharField(max_length=40)
	photo = models.ImageField(upload_to='Proveedor/%Y/%m/%d', blank=True, null=True)


	def __str__(self):
		return self.empresa

	class Meta:
		verbose_name = 'Proveedor'
		verbose_name_plural = 'Proveedores'
		ordering = ['nombre']