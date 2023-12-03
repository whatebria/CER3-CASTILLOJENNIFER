from django.shortcuts import render
from .models import Evento, Segmento
from datetime import date


# Create your views here.

def homePublico(request):
    title = 'Home'
    año = '2023'
    fecha_actual = date.today()
    eventosProfesor = Evento.objects.filter(segmento = 3)[:4]
    eventosJefe = Evento.objects.filter(segmento = 4)[:4]
    tipo = Evento.TIPO_CHOICES

    data = {
        'title': title,
        'Eventos': Evento.objects.all(),
        'Segmento': Segmento.objects.all(),
        'año': año,
        'eventosProfesor': eventosProfesor,
        'eventosJefe': eventosJefe,
        'fecha_actual': fecha_actual,
        'Tipos': tipo,
    }
    return render(request, 'app/home.html', data)


def filtrarSegmento(request):
    title = 'FiltrarSegmento'
    fecha_actual = date.today()
    tipo = Evento.TIPO_CHOICES
    eventosProfesor = Evento.objects.filter(segmento = 3)[:4]
    eventosJefe = Evento.objects.filter(segmento = 4)[:4]


    segmento_seleccionado = request.GET.get('filtroPorSegmento')
    if segmento_seleccionado == 0 or segmento_seleccionado is None:
        eventos = Evento.objects.all()
    else:
        eventos = Evento.objects.filter(segmento = segmento_seleccionado)
    año = 2023
    data = {
        'title': title,
        'Eventos': eventos,
        'Segmento': Segmento.objects.all(),
        'año': año,
        'Tipos': tipo,
        'eventosJefe': eventosJefe,
        'eventosProfesor': eventosProfesor,
        'fecha_actual': fecha_actual,
        'fecha_actual': fecha_actual,
    }

    return render(request, 'app/home.html', data)

def filtrarTipo(request):
    tipo = Evento.TIPO_CHOICES
    eventosProfesor = Evento.objects.filter(segmento = 3)[:4]
    eventosJefe = Evento.objects.filter(segmento = 4)[:4]


    title = 'FiltrarTipo'
    flag = False
    tipo = Evento.TIPO_CHOICES
    fecha_actual = date.today()

    
    tipo_seleccionado = request.GET.get('tipo')
    posicion = 0
    while flag == False:
        tipo_temp = Evento.TIPO_CHOICES[posicion]
        if tipo_temp[1] == tipo_seleccionado:
            coso = tipo_temp
            flag = True
        else:
            posicion += 1

    if tipo_seleccionado == 0 or tipo_seleccionado is None:
        eventos = Evento.objects.all()
    else:
        eventos = Evento.objects.filter(tipo = Evento.TIPO_CHOICES[posicion][0])

    año = 2023
    data = {
        'title': title,
        'Eventos': eventos,
        'Segmento': Segmento.objects.all(),
        'año': año,
        'Tipos': tipo,
        'eventosJefe': eventosJefe,
        'eventosProfesor': eventosProfesor,
        'fecha_actual': fecha_actual,
        'fecha_actual': fecha_actual,
    }
    return render(request, 'app/home.html', data)