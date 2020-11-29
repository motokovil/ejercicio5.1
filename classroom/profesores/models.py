from django.db import models
from materias.models import Materia
# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    clase = models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __str__(self):
        self.nombre