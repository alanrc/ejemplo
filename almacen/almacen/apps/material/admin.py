from django.contrib import admin

from almacen.apps.material.models import *

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(UnidadMedida)
admin.site.register(Almacen)
admin.site.register(Material)
admin.site.register(Ingreso)
admin.site.register(Salida)
