# Generated by Django 3.0.4 on 2020-05-01 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contratante',
            fields=[
                ('id_contratante', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_contratante', models.CharField(max_length=50, verbose_name='Nombres')),
                ('ape_contratante', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('cedu_contratante', models.CharField(max_length=15, verbose_name='Identificación')),
                ('celu_contratante', models.CharField(max_length=10, verbose_name='Numero de Celular')),
                ('email_contratante', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Contratos_Externos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_contrato', models.CharField(max_length=50, verbose_name='Tipo de Contrato')),
                ('objeto_contrato', models.CharField(max_length=50, verbose_name='Objeto Del Contrato')),
                ('doc_contrato', models.FileField(upload_to='contratos_externos', verbose_name='Documento')),
                ('fech_inicio_contrato', models.DateField(verbose_name='Fecha de Inicio')),
                ('fech_fin_contrato', models.DateField(verbose_name='Fecha Final')),
                ('contratante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='REGContracEx.Contratante')),
            ],
        ),
    ]