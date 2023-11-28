from rest_framework import viewsets
from .serializers import EventoSerializer
from app.models import Evento
from rest_framework.permissions import DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class EventoViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]

    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]

    filterset_fields = {
        'fecha_inicio': ['year'],
        'tipo': ['exact'],
        'segmento': ['contains'],
    }
