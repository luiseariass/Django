import os
from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
	
	def __init__(self, nombre,apellido):
		
		self.nombre = nombre
		self.apellido = apellido

def saludo(request):
    # Entrar al directorio de plantillas
    script_dir = os.path.dirname(__file__)
    rel_path = "../Plantillas/primera.html"
    abs_file_path = os.path.join(script_dir, rel_path)
    doc_externo = open(abs_file_path)
    plant = Template(doc_externo.read())
    doc_externo.close()
    p1= Persona("Luis Enrique","Arias Serrano")
    ahora = datetime.datetime.now()
    #temas=["Plantillas","Modelos","Formulario","Vistas","Aplicaciones"]
    temas=[]
    cnt = Context({'Nombre_programador': p1.nombre,
                   'Apellido_programador': p1.apellido,'Ahora':ahora,"Temas":temas})
    
    documento = plant.render(cnt)

    return HttpResponse(documento)


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
