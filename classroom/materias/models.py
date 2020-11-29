from django.db import models

# Create your models here.
class Materia(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        self.nombre