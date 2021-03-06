from django.shortcuts import render
from django.http import HttpResponse
from Gestion_Pedidos.models import Articulos 

def busqueda_producto(resquest):

	return render(resquest,'primera.html')


def buscar_art(request):
	if request.GET['prod']:
		#mensaje = "Articulo buscado: %r" %request.GET["prod"]
		prod = request.GET['prod']
		if len(prod)>20:
		
			return render(request,'resultado_busqueda_larga.html')
		else:

			articulos=Articulos.objects.filter(nombre__icontains=prod)
			tamano = articulos.count()
		
			return render (request,'resultado_busqueda.html',{'articulos':articulos,'query':prod,'tamano':tamano,'caso':0})
	else: 	
		return render(request,'resultado_busqueda_vacia.html')


def buscar_sec(request):
	if request.GET['sec']:
		#mensaje = "Articulo buscado: %r" %request.GET["prod"]
		sec = request.GET['sec']
		if len(sec)>20:

			return render(request,'resultado_busqueda_larga.html')
		
		else:
			seccion=Articulos.objects.filter(seccion__icontains=sec)
			tamano = seccion.count()
			return render (request,'resultado_busqueda.html',{'seccion':sec,'query':seccion,'tamano':tamano,'caso':1})
	else: 	
		return render(request,'resultado_busqueda_vacia.html')		


def contacto(request):
	
	return render(request,'contacto.html')		