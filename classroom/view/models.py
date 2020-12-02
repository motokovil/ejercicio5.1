from django.db import models

# Create your models here.
class View(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        self.nombre

