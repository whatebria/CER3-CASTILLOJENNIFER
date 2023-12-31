# Generated by Django 4.2.6 on 2023-11-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Segmento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('V', 'Vacaciones'), ('F', 'Feriado'), ('SA', 'Suspension actividades'), ('SAPM', 'Suspension actividades PM'), ('PL', 'Periodo Lectivo'), ('SE', 'Suspension evaluaciones'), ('C', 'Ceremonia'), ('E', 'EDDA'), ('Ev', 'Evaluacion'), ('Ay', 'Ayudantias'), ('H', 'Hito academico'), ('S', 'Secretaria Academica'), ('OAI', 'OAI')], default='-', max_length=30)),
                ('fecha_actual', models.DateField(auto_now=True)),
                ('segmento', models.ManyToManyField(to='app.segmento')),
            ],
        ),
    ]
