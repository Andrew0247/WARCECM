from django.db import models

# Create your models here.

class Empleado(models.Model):
    id_empleado=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nom_empleado=models.CharField(max_length=50, verbose_name="Nombres")
    ape_empleado=models.CharField(max_length=50, verbose_name="Apellidos")
    cedu_empleado=models.CharField(verbose_name="Identificación", max_length=15)
    celu_empleado=models.CharField(verbose_name="Numero de Celular", max_length=10)
    email_empleado=models.EmailField(verbose_name="Email")
    #Elimine la contraseña
    #passw_empleado=models.CharField(max_length=30, verbose_name="Contraseña")
    estado_empleado=models.BooleanField(verbose_name="Actualmente Contratado")

    def __str__(self):
        return "{} {} {}".format(self.cedu_empleado,self.nom_empleado,self.ape_empleado)

# ============= Junte las tablas Tipo_COntrato, Cargo_Empleado y Contratos_Doc, ===============
# ========== para crear una sola tabla que junta los atributos de todas las 3 tablas ==========
class Contratacion(models.Model):
    empleado=models.OneToOneField(Empleado, null=True, blank=True, on_delete=models.CASCADE)
    objeto_contrato=models.CharField(max_length=80, verbose_name="Objeto del Contrato")
    clase_contrato=models.CharField(max_length=80, verbose_name="Clase de Contrato")
    valor_contrato=models.CharField(max_length=10, verbose_name="Valor del Contrato")
    contrato_doc=models.FileField(upload_to='contratos', verbose_name="Contrato")
    dura_contrato=models.IntegerField(verbose_name="Duración del Contrato")
    fech_inicio_contrato=models.DateField(verbose_name="Fecha de Inicio")
    fech_fin_contrato=models.DateField(verbose_name="Fecha Final")
    supervisor=models.CharField(max_length=80, verbose_name="Supervisor")

    def __str__(self):
       return self.objeto_contrato

class Educacion(models.Model):
    empleado=models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)
    nom_instituto=models.CharField(max_length=50, verbose_name="Nombre de la Institución")
    niv_educativo=models.CharField(max_length=50, verbose_name="Nivel Educativo")
    deta_educacion=models.CharField(max_length=50, verbose_name="Programa")
    cursa_educacion=models.BooleanField(verbose_name="Cursando Actualmente")
    fech_inicio_edu=models.DateField(verbose_name="Fecha de Inicio")
    fech_fin_edu=models.DateField(verbose_name="Fecha Final")

    def __str__(self):
        return self.nom_instituto

# ============= Junte las tablas Experiencia_Laboral y Certificacion_Laboral, ===============
# ========== para crear una sola tabla que junta los atributos de las 2 tablas  =============
class Experiencia_Laboral(models.Model):
    empleado=models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)
    nom_empresa=models.CharField(max_length=50, verbose_name="Nombre de la empresa")
    cargo_experiencia=models.CharField(max_length=50, verbose_name="Cargo desempeñado")
    dura_experiencia=models.IntegerField(verbose_name="Duracion de la experiencia")
    certificacion_labo=models.FileField(upload_to='certificacion', verbose_name="Documento")
    fech_inicio_expe=models.DateField(verbose_name="Fecha de Inicio")
    fech_fin_expe=models.DateField(verbose_name="Fecha Final")

    def __str__(self):
        return self.nom_empresa

# ============= Modifique la tabla Hojas_Vida, para crear una tabla donde se subiria ===============
# =============                   los documentos de soporte                          ===============
class Documentos_Soporte(models.Model):
    empleado=models.OneToOneField(Empleado, null=True, blank=True, on_delete=models.CASCADE)
    tipo_documento=models.CharField(max_length=50, verbose_name="Tipo de Documento")
    documento_soporte=models.FileField(upload_to='documentos_soporte', verbose_name="Documento")

    def __str__(self):
        return self.tipo_documento

class Valoracion(models.Model):
    empleado=models.OneToOneField(Empleado, null=True, blank=True, on_delete=models.CASCADE)
    valoracion=models.FloatField()
    observacion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.valoracion