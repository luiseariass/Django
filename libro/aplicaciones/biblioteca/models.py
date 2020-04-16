from django.db import models

class Autor(models.Model):
	nombre = models.CharField('Nombre',max_length=80)
	nacionalidad = models.CharField('Nacionalidad', blank=True, max_length=50)

	def __str__(self):
		return self.nombre

class Libros(models.Model):
	titulo = models.CharField('Titulo',max_length=150)
	resumen = models.TextField('Resumen',blank=True)
	autor  = models.ForeignKey(Autor,on_delete= models.CASCADE)

	def __str__(self):
		return self.titulo
							