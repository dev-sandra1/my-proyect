from django.db import models
from .models import Categoria, Producto

class Categoria(models.Model):
  nombre = models.ChaField(max_legth=255)

def __str__(self):
        return self.nombre
  
class Producto(models.Model):
  nombre = models.ChaField(max_legth=255)
  stock = models.IntegerField()
  puntaje = models.FloatField()
  categoria = models.ForeignKey()



admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
