# La Máquina del Tiempo - Proyecto de Presupuestos

La máquina del tiempo
la empresa fue creada con el objetivo de crear relojes de diferentes épocas y estilos para su
posterior venta a distintos proveedores.
Es una empresa que refleja la evolución entre el diseño, la tecnología y la visualización tiempo.
Para cumplir con la misión de la empresa se realizaron diferentes investigaciones y selecciones de la calidad de los relojes, permitiendo crear con éxito la empresa y abriendo las puertas al público, la máquina del tiempo se a convertido en una empresa muy popular para los amantes de los
relojes de calidad.

## Objetivo del Proyecto

El objetivo de este proyecto es desarrollar un sistema de facturación que permita gestionar los productos y generar presupuestos para los clientes, solicitando los datos necesarios de la empresa dando la opcion de poder descargar la cotizacion en formato pdf para asi poder dar una mayor seguridad de los precios y no sufra modificaciones en su orden 

# Aclaraciones Adicionales

El proyecto se desarrollará utilizando Python como lenguaje de programación y el framework Django. La instalación y configuración de Python y Django se proporcionarán en el archivo README.md del proyecto para facilitar su implementación y ejecución.

Con este alcance del proyecto, se espera lograr un sistema robusto y eficiente que satisfaga las necesidades de facturación y presupuestos de "La Máquina del Tiempo", contribuyendo así al éxito y crecimiento continuo de la empresa.


## Requisitos

### Requisitos Funcionales

1. **Gestión de Productos:**
     visualización de productos.

3. **Gestión de Facturas:**
     Cálculo automático de impuestos y totales.

5. **Acceso y Seguridad:**
     Autenticación segura de usuarios.
     Registro de actividad de los usuarios.

### Requisitos No Funcionales

1. **Rendimiento:**
   

2. **Escalabilidad:**
   
     Diseño modular para facilitar la adición de nuevas funcionalidades.

3. **Seguridad:**
     Cifrado de datos sensibles.
     Protección contra ataques comunes.

4. **Disponibilidad:**
     Alta disponibilidad (99.9% de tiempo de actividad).
     

5. **Usabilidad:**
     Interfaz intuitiva y fácil de usar.

6. **Compatibilidad:**
     Compatible con principales navegadores (Chrome, Firefox, Safari, Edge).
   
8. **Mantenimiento:**
     Documentación clara y detallada.
   
9. **Sistema de fácil uso:**
     Simplificación en la navegación y uso del sistema.

## Tecnologías Utilizadas

- **Lenguaje de Programación:** Python
- **Framework:** Django
- **Base de datos:** sqllite3

## Instalación

### Instalación de Python

1. Descarga e instala Python desde la página oficial: [Python Downloads](https://www.python.org/downloads/)

### Ingresar a nuestro proyecto

1.	Abre el cmd y navega a la carpeta donde deseas crear el proyecto.
2.	Ejecuta los siguientes comandos para poder levantar el proyecto Django

```bash

debemos abrir el visual studio code
presionar ctrl ñ para abrir la termina luego debemos ejecutar el comando 
git clone https://github.com/marcelaGonzalezArancibia/proyecto_time.git (en el cual podremos descargar el proyecto en nuestra computadora)
los siguentes pasos son  
1. Crear un entorno virtual:
Python -m venv nombre_del_entorno
Activar el entorno virtual:
En Windows: nombre_del_entorno\Scripts\activate
En macOS/Linux: source nombre_del_entorno/bin/activateInstalar Django.
2. Instalar Django: pip install django
3.Ejecutar el Servidor de Desarrollo (cd nombre_del_proyecto) (Python manage.py runserver)
4. Crear una Aplicación Django: (Python manage.py startapp nombre_de_la_aplicacion)
5. Ejecutar Migraciones de la Base de Datos (Python manage.py makemigrations) (Python manage.py migrate)
6. Crear un Superusuario (Python manage.py createsuperuser)
7.Ejecutar el Servidor de Desarrollo y Acceder a la Interfaz de Administración (Python manage.py runserver)
8. instalar para poder desagar en formato pdf (pip install xhtml2pdf)
 



