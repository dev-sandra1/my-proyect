from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import ProductoForm
from .models import Producto

def index(request): 
   productos = Producto.objects.all()

   return render(
      request,
      'index.html',
      context={'productos': productos}
   )

def detalle(request, producto_id):
      producto = get_object_or_404(Producto, id=producto_id)
      producto = Producto.objects.get(id=producto_id)

      return render(
      request,
     'detalle.html',
     context={'producto': producto})

def formulario(request):
      if request.method == 'POST':
          form = ProductoForm(request.POST)
          if form.is_valid():
              form.save()
              return HttpResponseRedirect('/Producto guardado')
      else: 
          form = ProductoForm()


      return render(
           request,
           'producto_form.html',
             {'form': form}
       )