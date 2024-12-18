from django.urls import path
from . import views

urlpatterns = [
    path('realizar/', views.realizar_pedido, name='realizar_pedido'),
    path('pedido-completado/', views.pedido_completado, name='pedido_completado'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('editar-pedido/<int:id>/', views.editar_pedido, name='editar_pedido'),
    path('eliminar-pedido/<int:id>/', views.eliminar_pedido, name='eliminar_pedido'),
]
