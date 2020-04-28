from django.urls import include,  path, re_path

import Gestion_Pedidos.views as views

app_nam = "Gestion_Pedidos_app"

urlpatterns = [path('busqueda-producto/',views.busqueda_producto,name='busqueda_prod'),
			path('buscar-art/',views.buscar_art,name='buscar_art'),
			path('buscar-sec/',views.buscar_sec,name='buscar_sec'),
			path('contacto/',views.contacto,name='contacto'),
]
