from django.contrib import models
from ..models import Categoria, Producto

class Categoria(admin.ModelAdmin):
     list_display = ('id', 'nombre')

class  Producto(admin.ModelAdmin):
     exclude = ('creado_en', )
     list_display = ('id', 'nombre', 'stock', 'creado_en')

# Register your models here.
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)