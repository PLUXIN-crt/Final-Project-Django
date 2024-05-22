from django.db import models

# Create your models here.
class Escuela(models.Model):
    nombre = models.CharField(max_length=50)
    activo = models.IntegerField()

    def __str__(self):
        return self.nombre

class Carrera(models.Model):
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    version = models.IntegerField()    
    activo = models.IntegerField()

    def __str__(self):
        return self.escuela.nombre + ' - ' + self.nombre







class Alumno(models.Model):
    rut   = models.CharField(primary_key=True, max_length=10)
    dv   = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    nacimiento = models.DateField()
    fono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    activo = models.IntegerField()

def __str__(self):
    return self.rut , '-',self.dv 