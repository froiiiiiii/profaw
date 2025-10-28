from django.db import models

# Entidad País (Apellidos del estudiante = Parraga)
class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# Entidad Estudiante (Nombre del estudiante = Pepe)
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='estudiantes')

    def __str__(self):
        return self.nombre
