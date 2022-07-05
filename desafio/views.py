from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from datetime import datetime

from .forms import BusquedaUsuario, FormUsuario



from .models import Prueba

# Create your views here.


def una_vista(request):
    return render(request, 'index.html')


def crear_dato(request):
    

    #print(request.GET)  
    #print(request.POST) 
    
    # nombre = request.POST.get("nombre")  
    # edad = request.POST.get("edad")  
    
    # usuario = Prueba(nombre=nombre, edad=edad , fecha_nacimiento=datetime.now())
    # usuario.save()
    
    
   if request.method == "POST":
       form = FormUsuario(request.POST)
       
       if form.is_valid():
           data = form.cleaned_data
           
           fecha = data.get("fecha_nacimiento")
           if  not fecha:
               fecha = datetime.now()
           
           
           
           usuario = Prueba(
               nombre= data.get("nombre"), 
               edad= data.get("edad"), 
               fecha_nacimiento=fecha
               #fecha_nacimiento=datetime.now()
               #fecha_nacimiento= fecha if fecha if else datetime.now()
               )
           usuario.save()
           
        #    listado_usuarios = Prueba.objects.all()
        #    form = BusquedaUsuario() 
        #    return render(request, "listado_usuarios.html", {"listado_usuarios": listado_usuarios, "form":form})
           return redirect("listado_usuarios")
       
        
       else:
            return render(request, 'crear_dato.html', {"form": form_usuario})
   
   
   form_usuario = FormUsuario()
    
   return render(request, 'crear_dato.html', {"form": form_usuario})



def listado_usuarios(request):
    
    nombre_de_busqueda = request.GET.get("nombre")
    
    if nombre_de_busqueda:
        listado_usuarios = Prueba.objects.filter(nombre__icontains=nombre_de_busqueda)
    else:   
         listado_usuarios = Prueba.objects.all()
         
    form = BusquedaUsuario() 
    return render(request, "listado_usuarios.html", {"listado_usuarios": listado_usuarios, "form":form})
