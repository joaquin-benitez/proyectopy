from django.urls import path
from . import views

urlpatterns = [
    path('realizar/', views.realizar_pedido, name='realizar_pedido'),
    path('pedido-completado/', views.pedido_completado, name='pedido_completado'),
    
]
