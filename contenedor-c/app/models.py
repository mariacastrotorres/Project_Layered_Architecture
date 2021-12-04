from peewee import Model, CharField
from db import db

class Mascota(Model):
	nombre = CharField()
	imagen = CharField()

	class Meta:
		database = db
		table_name = 'mascota'

	def __str__(self):
		return f"ID: {self.id} - Nombre: {self.nombre} - Imagen: {self.imagen}"

class Persona(Model):
	nombre = CharField()
	apellido = CharField()
	imagen = CharField()

	class Meta:
		database = db
		table_name = 'persona'

	def __str__(self):
		return f"ID: {self.id} - Nombre: {self.nombre} - Apellido: {self.apellido} - Imagen: {self.imagen}"