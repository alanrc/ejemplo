from django.db import models
from almacen.apps.proveedor.models import Proveedor
from almacen.apps.funcionario.models import Funcionario

class Marca(models.Model):
	nombre = models.CharField(max_length=50,unique=True)
	descripcion = models.TextField(blank=True, null=True)

	class Meta:
		verbose_name = "Marca"
		verbose_name_plural = "Marcas"
		ordering = ['nombre']


	def __str__(self):
		return self.nombre

class Categoria(models.Model):
	nombre = models.CharField(max_length=50, unique=True)
	descripcion = models.TextField(blank=True, null=True)

	class Meta:
		verbose_name = "Categoria"
		verbose_name_plural = "Categorias"
		ordering = ['nombre']

	def __str__(self):
		return self.nombre

class UnidadMedida(models.Model):
	nombre = models.CharField(max_length=50, unique=True)
	descripcion = models.TextField(blank=True, null=True)

	class Meta:
		verbose_name = "Unidad de Medida"
		verbose_name_plural = "Unidad de Medidas"
		ordering = ['nombre']

	def __str__(self):
		return self.nombre

class Almacen(models.Model):
	nombre = models.CharField(max_length=50, unique=True)
	descripcion = models.TextField(blank=True, null=True)

	class Meta:
		verbose_name = "Almacen"
		verbose_name_plural = "Almacenes"
		ordering = ['nombre']

	def __str__(self):
		return self.nombre


class Material(models.Model):
	nombre = models.CharField(max_length=50)
	marca = models.ForeignKey(Marca)
	categoria = models.ForeignKey(Categoria)
	unidad_medida = models.ForeignKey(UnidadMedida)
	almacen = models.ForeignKey(Almacen)
	proveedor = models.ForeignKey(Proveedor)
	stock_actual = models.PositiveIntegerField(verbose_name='Stock Actual', default='0')

	class Meta:
		verbose_name = "Material"
		verbose_name_plural = "Materiales"
		ordering = ['id']

	def __str__(self):
		return self.nombre

class Ingreso(models.Model):
	material = models.ForeignKey(Material)
	cantidad = models.PositiveIntegerField()
	precio_u = models.DecimalField(max_digits=7, decimal_places=2)
	precio_t = models.DecimalField(max_digits=7, decimal_places=2)
	num_factura = models.CharField(max_length=10, unique=True)
	serie = models.CharField(max_length=15, blank=True, null=True)
	codigo = models.CharField(max_length=15, blank=True, null=True)
	objeto = models.TextField(blank=True, null=True)
	observacion = models.TextField(blank=True, null=True)
	fecha_i = models.DateField(auto_now_add=True)
	funcionario = models.ForeignKey(Funcionario)

	total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

	class Meta:
		verbose_name='Ingreso'
		verbose_name_plural='Ingresos'
		ordering = ['-fecha_i']

	def __str__(self):
		return '%s %s %s %s' % (self.cantidad, self.precio_u, self.precio_t, self.num_factura)

class Salida(models.Model):
	material = models.ForeignKey(Material)
	ingreso = models.ForeignKey(Ingreso)
	funcionario = models.ForeignKey(Funcionario)
	cantidad = models.PositiveIntegerField()
	#precio_t = models.DecimalField(max_digits=7, decimal_places=2)
	objeto = models.TextField(blank=True, null=True)
	observacion = models.TextField(blank=True, null=True)
	fecha = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = 'Salida'
		verbose_name_plural = 'Salidas'
		ordering = ['-fecha']

	def __str__(self):
		return self.cantidad


class Detalle(models.Model):
	ingreso = models.ForeignKey(Ingreso)
	salida = models.ForeignKey(Salida)

	def __str__(self):
		return '%s %s' % (self.ingreso, self.salida)


