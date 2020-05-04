# Generated by Django 3.0.4 on 2020-05-03 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jefe',
            fields=[
                ('id_jefe', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_jefe', models.CharField(max_length=50, verbose_name='Nombres')),
                ('ape_jefe', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('cedu_jefe', models.CharField(max_length=15, verbose_name='Identificación')),
                ('celu_jefe', models.CharField(max_length=10, verbose_name='Numero de Celular')),
                ('email_jefe', models.EmailField(max_length=254, verbose_name='Email')),
                ('estado_jefe', models.BooleanField(verbose_name='Actualmente Contratado')),
            ],
        ),
        migrations.CreateModel(
            name='Valoracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valoracion', models.FloatField()),
                ('observacion', models.CharField(max_length=100)),
                ('empleado', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='REGJefes.Jefe')),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia_Laboral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_empresa', models.CharField(max_length=50, verbose_name='Nombre de la empresa')),
                ('cargo_experiencia', models.CharField(max_length=50, verbose_name='Cargo desempeñado')),
                ('dura_experiencia', models.IntegerField(verbose_name='Duracion de la experiencia')),
                ('certificacion_labo', models.FileField(upload_to='certificacion', verbose_name='Documento')),
                ('fech_inicio_expe', models.DateField(verbose_name='Fecha de Inicio')),
                ('fech_fin_expe', models.DateField(verbose_name='Fecha Final')),
                ('empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='REGJefes.Jefe')),
            ],
        ),
        migrations.CreateModel(
            name='Educacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_instituto', models.CharField(max_length=50, verbose_name='Nombre de la Institución')),
                ('niv_educativo', models.CharField(max_length=50, verbose_name='Nivel Educativo')),
                ('deta_educacion', models.CharField(max_length=50, verbose_name='Programa')),
                ('cursa_educacion', models.BooleanField(verbose_name='Cursando Actualmente')),
                ('fech_inicio_edu', models.DateField(verbose_name='Fecha de Inicio')),
                ('fech_fin_edu', models.DateField(verbose_name='Fecha Final')),
                ('empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='REGJefes.Jefe')),
            ],
        ),
        migrations.CreateModel(
            name='Documentos_Soporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(max_length=50, verbose_name='Tipo de Documento')),
                ('documento_soporte', models.FileField(upload_to='documentos_soporte', verbose_name='Documento')),
                ('empleado', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='REGJefes.Jefe')),
            ],
        ),
        migrations.CreateModel(
            name='Contratacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo_empleado', models.CharField(max_length=50, verbose_name='Cargo')),
                ('tipo_contrato', models.CharField(max_length=50, verbose_name='Tipo de Contrato')),
                ('contrato_doc', models.FileField(upload_to='contratos', verbose_name='Contrato')),
                ('fech_inicio_contrato', models.DateField(verbose_name='Fecha de Inicio')),
                ('fech_fin_contrato', models.DateField(verbose_name='Fecha Final')),
                ('empleado', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='REGJefes.Jefe')),
            ],
        ),
    ]
