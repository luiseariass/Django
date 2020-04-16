import os
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render
class Persona(object):
	
	def __init__(self, nombre,apellido):
		
		self.nombre = nombre
		self.apellido = apellido

def saludo(request):
    p1= Persona("Luis Enrique","Arias Serrano")
    ahora = datetime.datetime.now()
    temas=["Plantillas","Modelos","Formulario","Vistas","Aplicaciones"]
    cnt = {'Nombre_programador': p1.nombre,'Apellido_programador': p1.apellido,'Ahora':ahora,"Temas":temas}
    return render(request,'primera.html',cnt)

def despedida(request):

    return HttpResponse('Chao mundo')


def damefecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html>
	<body>
	<h2>
	Fecha y hora actual %s
	</h2>
	</body>
	</html>""" % fecha_actual
    return(HttpResponse(documento))


def calculaedad(request, agno):

    edadactual = 25
    periodo = agno - 2020
    EdadFutura = edadactual + periodo
    documento = """<html>
	<body>
	<h2>
	En el año %s tendras %s años
	</h2>
	</body>
	</html>""" % (agno, EdadFutura)
    return(HttpResponse(documento))


def Curso_Django(request):
	p1= Persona("Pildora","Informativa")
	cnt={'Profesor':p1}
	
	return render(request,"Curso_Django.html",cnt)

def Curso_PHP(request):
	p1= Persona("Victor","Robles")
	cnt={'Profesor':p1}
	
	return render(request,"Curso_PHP.html",cnt)
		