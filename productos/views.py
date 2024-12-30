from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto

def index(request): 
   productos = Producto.objects.all().values()
  #print(productos) 
   return JsonResponse(list(productos), safe=False)