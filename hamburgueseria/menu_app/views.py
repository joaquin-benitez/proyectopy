from django.shortcuts import render
from .models import Hamburguesa, QuienesSomos


def menu_view(request):
    hamburguesas = Hamburguesa.objects.all()
    return render(request, 'menu_app/menu.html', {'hamburguesas': hamburguesas})

def quienes_somos_view(request):
    quienes_somos = QuienesSomos.objects.first()
    return render(request, 'menu_app/quienes_somos.html', {'quienes_somos': quienes_somos})

