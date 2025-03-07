DjangoEquipoCRUD
Este es un proyecto CRUD (Crear, Leer, Actualizar, Eliminar) desarrollado en Django que permite gestionar equipos. El proyecto incluye funcionalidades básicas para agregar, ver, editar y eliminar equipos desde una interfaz web.

Características
CRUD de Equipos: Permite crear, leer, actualizar y eliminar equipos.

Interfaz Web: Interfaz sencilla y fácil de usar.

Base de Datos: Utiliza SQLite como base de datos por defecto.

Autenticación: Incluye autenticación de usuarios para acceder a las funcionalidades.

Requisitos Previos
Antes de comenzar, asegúrate de tener instalado lo siguiente:

Python 3.x

Pip (Gestor de paquetes de Python)

Virtualenv (opcional, pero recomendado)

Instalación
Sigue estos pasos para configurar el proyecto en tu entorno local:

1-Clona el repositorio:
Copy
git clone https://github.com/LuisMiraglio/DjangoEquipoCRUD.git
cd DjangoEquipoCRUD

2-Crea un entorno virtual (opcional pero recomendado):
Copy
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

3-Instala las dependencias:
Copy
pip install -r requirements.txt

4-Realiza las migraciones:
Copy
python manage.py migrate

5-Crea un superusuario (para acceder al panel de administración):
Copy
python manage.py createsuperuser

6-Inicia el servidor de desarrollo:
Copy
python manage.py runserver

7-Accede a la aplicación:
Abre tu navegador y visita http://127.0.0.1:8000/.

8-Uso
Panel de Administración: Accede a http://127.0.0.1:8000/admin para gestionar los equipos y usuarios.

Interfaz de Usuario: Navega por la interfaz web para ver, agregar, editar y eliminar equipos.

Estructura del Proyecto
Copy
DjangoEquipoCRUD/
├── manage.py
├── equipo/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── DjangoEquipoCRUD/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── requirements.txt

Contribución
Si deseas contribuir a este proyecto, sigue estos pasos:

Haz un fork del repositorio.

Crea una rama para tu nueva funcionalidad (git checkout -b feature/nueva-funcionalidad).

Realiza tus cambios y haz commit (git commit -m 'Añade nueva funcionalidad').

Sube tus cambios (git push origin feature/nueva-funcionalidad).

Abre un Pull Request.

Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

Contacto
Si tienes alguna pregunta o deseas ponerte en contacto conmigo, puedes enviarme un correo a: miraglioluis1@gmail.com
