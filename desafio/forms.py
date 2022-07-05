
from django import forms


class FormUsuario(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(required=False)
    
    
    
class BusquedaUsuario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
    


    
     
