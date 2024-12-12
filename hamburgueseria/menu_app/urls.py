from django.urls import path
from .views import menu_view, quienes_somos_view


urlpatterns = [
    path('', menu_view, name='menu'),
    path('quienes-somos/', quienes_somos_view, name='quienes_somos'),
    
]
