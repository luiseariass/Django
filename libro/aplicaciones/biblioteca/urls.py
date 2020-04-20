from django.urls import include,  path, re_path

import aplicaciones.biblioteca.views as views

app_nam = "bibliotecas_app"

urlpatterns = [path('autores/',views.Lista_Autores.as_view(),name='lista-autores')
]
