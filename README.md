# WARCECM
Proyecto de un Aplicativo Web el cual lleva un registro de empleados, los respectivos jefes de los empleados, y los contratos externos a la empresa.

El siguiente proyecto esta realizado con el Framework Django (https://docs.djangoproject.com/en/3.0/). En este proyecto se hace uso de la biblioteca "bootstrap_modal_forms" para realizar el manejo de Modales, esta biblioteca se la puede descargar de la siguiente forma:

<Code>pip install bootstrap_modal_forms</Code>

Tambien se hace uso de Bootstrap 4.0, el cual se lo puede descargar o encontrar en el siguiente enlace <a href="https://getbootstrap.com/">Bootstrap</a>.

Al igual se hace un respectivo uso de JQuery, tambien se usa bibliotecas de jquery tales como <a href="https://cdnjs.com/libraries/jquery-datetimepicker">datetimepicker</a>, la cual es para personalizar la insercion de las fechas usando un calendario.

Para el manejo de los usuarios, se utiliza el modelo que el mismo Framework ofrece y genera. El cual se importa de la siguiente manera:

<Code>from django.contrib.auth.models import User</Code>

La carpeta del proyecto es la que tiene por nombre RegContrac, la cual contiene diferentes carpetas: 
<ul>
  <li>Bootstrap, la cual contiene archivos locales para utilizar Bootstrap.</li>
  <li>Portafolio, donde se encuentran diferentes carpetas en las que se encuentran las diferentes imagenes, archivos css, js, fuentes, etc.</li>
  <li>Archivos, en donde se almacenan los diferentes documentos que se suben utilizando los formularios.</li>
  <li>RegContrac, la cual es la carpeta donde estan las diferentes configuraciones propiamente del proyecto y en donde añadimos las aplicaciones que necesitamos para nuestro proyecto, estas estan en el archivo <Code>settings.py</Code>. Tambien las URLs para redireccionar a cada aplicacion, las cuales estan en el archivo <Code>urls.py</Code>
  <li>LRUsuarios, se configura toda la parte de los usuarios.</li>
  <li>REGContracEx, donde se realizan las configuraciones para la aplicacion que maneja la parte de los contratos externos.</li>
  <li>REGEmpleados, donde esta toda la parte de la configuracion de la aplicacion para el manejo de los Empleados y su respectivo registro.</li>
  <li>REGJefes, donde se configura todo el registro de los Jefes de los Empleados.</li>
</ul>

Tambien se hace uso de un metodo de Django el cual es <Code>send_mail()</Code>, este es importado con la siguiente instruccion <Code>from django.core.mail import send_mail</Code> en nuestro archivo <Code>views.py</Code>.
