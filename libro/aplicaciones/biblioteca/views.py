from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, UpdateView, DeleteView,)
from .models import Autor, Libros
from django.urls import reverse, reverse_lazy

#############
class Lista_Autores(ListView):
	template_name = "biblioteca/lista-autores.html"
	model = Autor
	context_object_name = 'autores'

class Lista_Libros(ListView):
	template_name = "biblioteca/lista-libros.html"
	context_object_name = 'libros'	

	def get_queryset(self):
		#Identificar  el autor
		id=self.kwargs['pk']
		#Filtro de los libros
		lista=Libros.objects.filter(autor=id)
		#Devuelvo la lista
		return lista
##########################

class Add_Autor(CreateView):
	template_name= 'biblioteca/add-autor.html'
	model = Autor
	fields = ['nombre','nacionalidad']
	success_url = '/'

class Autor_Update(UpdateView):
    template_name= 'biblioteca/update-autor.html'
    model = Autor
    fields = ['nombre','nacionalidad']
   

class Autor_Delete(DeleteView):
    template_name= 'biblioteca/delete-autor.html'
    model = Autor
    success_url = reverse_lazy('lista-autores')


########################################

class Add_Libro(CreateView):
	template_name= 'biblioteca/add-libros.html'
	model = Libros
	fields = ['titulo','resumen','autor']
	success_url = '.'	

