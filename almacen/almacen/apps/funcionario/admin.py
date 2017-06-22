from django.contrib import admin
from almacen.apps.funcionario.models import Funcionario, Departamento

admin.site.register(Funcionario)
admin.site.register(Departamento)