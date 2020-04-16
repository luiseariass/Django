from django.urls import include,  path, re_path

import aplicaciones.home.views as views

app_nam = "home_app"

urlpatterns = [path('index/', views.IndexView.as_view(), name="index"), 
				path('libros/',views.Lista_Libros.as_view(),name='lista')
]
