from django.urls import include,  path, re_path

import aplicaciones.biblioteca.views as views

app_nam = "bibliotecas_app"

urlpatterns = [path('',views.Lista_Autores.as_view(),name='lista-autores'),
			   path('lista-libros/<pk>/',views.Lista_Libros.as_view(),name='lista-libro'),
			   path('autor/add/',views.Add_Autor.as_view(),name='add-autor'),
			   path('libros/add/',views.Add_Libro.as_view(),name='add-libros'),
			   path('autor/<int:pk>/update/',views.Autor_Update.as_view(),name='update-autor'),
			   path('autor/<int:pk>/delete/',views.Autor_Delete.as_view(),name='delete-autor'),

]
