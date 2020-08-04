from django.db import models

# Create your models here.

class Contratante(models.Model):
    id_contratante=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nom_contratante=models.CharField(max_length=50, verbose_name="Nombres")
    ape_contratante=models.CharField(max_length=50, verbose_name="Apellidos")
    cedu_contratante=models.CharField(verbose_name="Identificación", max_length=15)
    celu_contratante=models.CharField(verbose_name="Numero de Celular", max_length=10)
    email_contratante=models.EmailField(verbose_name="Email")

    def __str__(self):
        return "{} {} {}".format(self.cedu_contratante,self.nom_contratante,self.ape_contratante)

class Contratos_Externos(models.Model):
    contratante=models.ForeignKey(Contratante, null=True, blank=True, on_delete=models.CASCADE)
    clase_contrato=models.CharField(max_length=50, verbose_name="Tipo de Contrato")
    objeto_contrato=models.CharField(max_length=50, verbose_name="Objeto Del Contrato")
    doc_contrato=models.FileField(upload_to='contratos_externos', verbose_name="Documento")
    fech_inicio_contrato=models.DateField(verbose_name="Fecha de Inicio")
    fech_fin_contrato=models.DateField(verbose_name="Fecha Final")
    supervisor=models.CharField(max_length=80 ,verbose_name="Supervisor")

    def __str__(self):
        return "{} {}".format(self.tipo_contrato,self.objeto_contrato)