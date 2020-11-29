from django.db import models
from materias.models import Materia
# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    clases = models.ManyToManyField(Materia, related_name='estudiantes')

    def __str__(self):
        self.nombre