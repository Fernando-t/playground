from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Prueba

# Create your views here.


def una_vista(request):
    return HttpResponse('<h1> Hola Hola Hola </h1>')


def un_template(request):
    
    #template = loader.get_template('index.html')
    
    prueba1 = Prueba(nombre = 'Fernando')
    prueba2 = Prueba(nombre = 'David')
    prueba3 = Prueba(nombre = 'Tino')
    
    prueba1.save()
    prueba2.save()
    prueba3.save()
    
    #render = template.render({'lista_objetos': [prueba1, prueba2, prueba3]})
    #return HttpResponse(render)
    
    return render(request, 'index.html', {'lista_objetos': [prueba1, prueba2, prueba3]})