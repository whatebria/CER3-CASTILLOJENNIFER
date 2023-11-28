from django.contrib import admin
from .models import Evento

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_filter = ['tipo', 'segmento', 'fecha_inicio']

admin.site.register(Evento, EventoAdmin)
