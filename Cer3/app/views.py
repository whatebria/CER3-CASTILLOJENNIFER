from django.shortcuts import render
from .models import Evento, Segmento, TIPO_CHOICES

# Create your views here.

def homePublico(request):
    title = 'Home'
    año = '2023'
    eventosProfesor = Evento.objects.filter(segmento = 3)[:4]
    eventosJefe = Evento.objects.filter(segmento = 4)[:4]

    data = {
        'title': title,
        'Eventos': Evento.objects.all(),
        'Segmento': Segmento.objects.all(),
        'año': año,
        'eventosProfesor': eventosProfesor,
        'eventosJefe': eventosJefe,
    }
    return render(request, 'app/home.html', data)


def filtrarSegmento(request):
    title = 'FiltrarSegmento'

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
    }

    return render(request, 'app/home.html', data)

def filtrarTipo(request):

    title = 'FiltrarTipo'
    flag = False
    
    tipo_seleccionado = request.GET.get('tipo')
    posicion = 0
    while flag == False:
        tipo_temp = TIPO_CHOICES[posicion]
        if tipo_temp[1] == tipo_seleccionado:
            wea = tipo_temp
            flag = True
        else:
            posicion += 1
    
    eventos = Evento.objects.filter(tipo = TIPO_CHOICES[posicion][0])

    año = 2023
    data = {
        'title': title,
        'Eventos': eventos,
        'Segmento': Segmento.objects.all(),
        'año': año,
    }
    return render(request, 'app/home.html', data)