# Generated by Django 4.2.6 on 2023-11-28 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_evento_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='fecha_actual',
        ),
    ]
