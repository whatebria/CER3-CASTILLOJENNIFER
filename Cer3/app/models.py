from collections.abc import Iterable
from django.db import models

# Create your models here.
TIPO_CHOICES = (
        ('V', 'Vacaciones'),
        ('F', 'Feriado'),
        ('SA', 'Suspension actividades'),
        ('SAPM', 'Suspension actividades PM'),
        ('PL', 'Periodo Lectivo'),
        ('SE', 'Suspension evaluaciones'),
        ('C', 'Ceremonia'),
        ('E', 'EDDA'),
        ('Ev', 'Evaluacion'),
        ('Ay', 'Ayudantias'),
        ('H', 'Hito academico'),
        ('S', 'Secretaria Academica'),
        ('OAI', 'OAI'),
    )

#SEGMENTO = (
 #   ('1', 'Comunidad USM'),
  #  ('2', 'Estudiante'),
   # ('3', 'Profesor'),
    #('4', 'Jefe de Carrera'),
    #)

class Segmento(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nombre

class Evento(models.Model):
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES, default='-')
    segmento = models.ManyToManyField(Segmento)
    fecha_actual = models.DateField(auto_now=True)
    

    def __str__(self) -> str:
        return self.titulo
    class Meta:
        models.Index(fields=["fecha_inicio", "fecha_termino", "titulo", "descripcion", "tipo", "segmento"])
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['fecha_inicio']