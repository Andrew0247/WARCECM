# WARCECM
Project of a Web Application which keeps a record of employees, the respective heads of employees, and external contracts to the company.

The following project is done with the <a href="https://docs.djangoproject.com/en/3.0/">Django Framework</a>. Postgresql is used as a database manager for the respective storage of the different registers. In this project, the "bootstrap_modal_forms" library is used to handle Modals. This library can be downloaded as follows:

<Code>pip install bootstrap_modal_forms</Code>

Bootstrap 4.0 is also used, which can be downloaded or found at the following link <a href="https://getbootstrap.com/">Bootstrap</a>.

Likewise, a respective use of JQuery is made, jquery libraries such as <a href="https://cdnjs.com/libraries/jquery-datetimepicker">datetimepicker</a> are also used, which is to personalize the insertion of the dates using a calendar.

For the management of users, the model that the same Framework offers and generates is used. Which is imported as follows:

<Code>from django.contrib.auth.models import User</Code>

The project folder is the one named RegContrac, which contains different folders: 
<ul>
  <li>Bootstrap, which contains local files to use Bootstrap.</li>
  <li>Portafolio, where there are different folders containing the different images, css files, js, fonts, etc.</li>
  <li>Archivos, where the different documents that are uploaded using the forms are stored.</li>
  <li>RegContrac, which is the folder where the different settings of the project are and where we add the applications we need for our project, they are in the file <Code>settings.py</Code>. Also the URLs to redirect to each application, which are in the file <Code>urls.py</Code>.
  <li>LRUsuarios, all the users part is configured.</li>
  <li>REGContracEx, where the settings are made for the application that handles the part of external contracts.</li>
  <li>REGEmpleados, where is all the part of the configuration of the application for the management of the Employees and their respective registration.</li>
  <li>REGJefes, where the entire registry of the Employees' Heads is configured.</li>
</ul>

We also make use of a Django method which is <Code>send_mail()</Code>, this is imported with the following instruction <Code>from django.core.mail import send_mail</Code> in our <Code>views.py</Code> file. Which is used to give notifications by email.
