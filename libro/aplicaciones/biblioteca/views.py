from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, )
from .models import Autor, Libros


class Lista_Autores(ListView):
	template_name = "biblioteca/lista-autores.html"
	model = Autor
	context_object_name = 'autores'