from django.db import models
from django.contrib.auth.models import User
from menu_app.models import Hamburguesa

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    hamburguesa = models.ForeignKey(Hamburguesa, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.usuario.username} - {self.hamburguesa.nombre}"
