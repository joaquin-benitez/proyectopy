from django.db import models

class Hamburguesa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre

class QuienesSomos(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

