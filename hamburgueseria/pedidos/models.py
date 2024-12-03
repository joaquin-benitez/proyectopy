from django.db import models

class Pedido(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.TextField()
    hamburguesa = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.nombre_usuario} - {self.hamburguesa} ({self.cantidad})"
