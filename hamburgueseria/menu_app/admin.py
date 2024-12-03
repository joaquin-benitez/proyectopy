from django.contrib import admin
from .models import Hamburguesa, QuienesSomos

admin.site.register(Hamburguesa)
admin.site.register(QuienesSomos)
class HamburguesaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'imagen')