from django.db import models

# Create your models here.

class Prueba(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True)
    
    def __str__(self):
        return f"Soy el usuario {self.nombre}"