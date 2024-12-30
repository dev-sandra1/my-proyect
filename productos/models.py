from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=180)

    def __str__(self): 
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=180)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    Categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    creado_en = models.DateTimeField(default=timezone.now) 

def __str__(self):
    return self.nombre
