from django.db import models

class Bodega(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre
