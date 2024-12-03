from django.urls import path
from .views import realizar_pedido

urlpatterns = [
    path('realizar/', realizar_pedido, name='realizar_pedido'),
]

