Descripción del proyecto

Este proyecto es una aplicación web en Django usando la libreria externa psutil que muestra información en tiempo real sobre:

1. Porcentaje de uso de la CPU
2. emoria RAM usada y total (en GB)
3. Uso del disco duro (usado, libre y total)
4. Cantidad de núcleos
5. Sistema operativo

Instrucciones claras para ejecutar el proyecto localmente

1. Clonar el repositorio: git clone https://github.com/dartgorsky/django-psutil-monitor.git
2. Entrar en la carpeta del proyecto: cd django-psutil-monitor
3. Crear un entorno virtual: python3 -m venv venv
4. Activar el entorno virtual: source venv/bin/activate
5. Instalar las dependencias: pip install -r requirements.txt
6. Correr el servidor: python manage.py runserver

Detalles sobre la instalación de dependencias (psutil, django):

Existen dos maneras para instalar las dependecias:

1. Dentro del entorno virtual instalar las dependecias creadas en el requirements.txt: pip install -r requirements.txt
2. Instalarlas manualmente pip install django y luego pip install psutil

Breve explicación de cada componente (vistas, plantillas, lógica de recolección):

Views.py

1. Calcula el porcentaje de uso de la CPU.
2. Obtiene la memoria RAM total, usada y su porcentaje.
3. Obtiene datos del disco duro (total, usado y libre).
4. Cuenta la cantidad de núcleos de la CPU.
5. Detecta el sistema operativo (Windows, Linux, etc.).

Toda esta información se envía a la plantilla HTML para mostrarla en pantalla.

Templates

Se crea un archivo index.html.
Muestra los datos recolectados en bloques llamados fieldsets para que se vea ordenado.
Incluye un botón para actualizar los datos manualmente.
Usa HTML5 y un diseño sencillo para que sea fácil de leer.

Lógica de recolección

La recolección de datos del sistema se hace con funciones de psutil:

1. psutil.cpu_percent() para la CPU.
2. psutil.virtual_memory() para la RAM.
3. psutil.disk_usage('/') para el disco duro.
4. psutil.cpu_count() para los núcleos.
5. platform.system() para el sistema operativo.

Se usa try-except para evitar errores si alguna información no se puede obtener, asegurando que la página siga funcionando sin fallos.

