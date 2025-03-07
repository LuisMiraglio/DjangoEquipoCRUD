# Proyecto CRUD para la administración de equipos

Este proyecto fue creado como prueba para exponer mis conocimientos en el framework Django. Es una aplicación web funcional que permite gestionar equipos mediante un sistema CRUD, con inicio de sesión y registro de usuarios.

## Funcionalidades

- **Autenticación de usuarios**: Registro e inicio de sesión.
- **Gestión de equipos**: Agregar, editar y eliminar equipos ZHONE con detalles como modelo, número de serie y dirección MAC.
- **Base de datos SQLite**: Utiliza SQLite para almacenar la información de los equipos.
- **Interfaz simple y funcional**: Diseño básico para interactuar con los equipos.

## Tecnologías

- **Backend**: Django
- **Base de datos**: SQLite
- **Autenticación**: Django Auth

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/LuisMiraglio/DjangoEquipoCRUD.git
    ```

2. Crea y activa un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Aplica las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

5. Ejecuta el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

Accede a la aplicación en `http://127.0.0.1:8000`.

## Contribuciones

Este proyecto fue creado como prueba personal, pero si deseas contribuir, puedes hacer un fork del repositorio y realizar mejoras.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de mi correo electrónico: [miraglioluis1@gmail.com](mailto:miraglioluis1@gmail.com).

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

