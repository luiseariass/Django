from django.contrib import admin
from Gestion_Pedidos.models import Clientes, Articulos,Pedidos

class Clientes_Admin(admin.ModelAdmin):
	list_display=('nombre','direccion','telefono')
	search_fields = ('nombre','telefono')	

class Articulos_Admin(admin.ModelAdmin):
	list_display=('nombre','seccion','precio')
	list_filter=('seccion',)

class Pedidos_Admin(admin.ModelAdmin):
	list_filter=('fecha',)
	date_hierarchy = 'fecha'


admin.site.register(Clientes,Clientes_Admin)
admin.site.register(Articulos,Articulos_Admin)
admin.site.register(Pedidos,Pedidos_Admin)
