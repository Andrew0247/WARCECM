# Generated by Django 3.0.4 on 2020-05-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REGEmpleados', '0004_contratacion_sueldo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contratacion',
            name='cargo_empleado',
        ),
        migrations.RemoveField(
            model_name='contratacion',
            name='sueldo',
        ),
        migrations.RemoveField(
            model_name='contratacion',
            name='tipo_contrato',
        ),
        migrations.AddField(
            model_name='contratacion',
            name='clase_contrato',
            field=models.CharField(default=None, max_length=80, verbose_name='Clase de Contrato'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contratacion',
            name='dura_contrato',
            field=models.IntegerField(default=None, verbose_name='Duración del Contrato'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contratacion',
            name='objeto_contrato',
            field=models.CharField(default=None, max_length=80, verbose_name='Objeto del Contrato'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contratacion',
            name='supervisor',
            field=models.CharField(default=None, max_length=80, verbose_name='Supervisor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contratacion',
            name='valor_contrato',
            field=models.CharField(default=None, max_length=10, verbose_name='Valor del Contrato'),
            preserve_default=False,
        ),
    ]
