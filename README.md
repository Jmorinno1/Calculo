# Sistema de Gestión de Recursos PMR

Este es un sistema completo para la gestión de recursos PMR (Personas con Movilidad Reducida) en aeropuertos. El sistema permite gestionar personal, asistencias, cálculos de recursos necesarios, vacaciones y más.

## Características principales

- Gestión completa de personal con todos los campos
- Registro y análisis de asistencias PMR
- Cálculos avanzados de recursos necesarios
- Gestión multi-aeropuerto
- Simulación de escenarios
- Importación de datos desde Excel
- Interfaz moderna con diseño responsivo

## Requisitos del sistema

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- SQLite (incluido) o PostgreSQL (opcional)
- Navegador web moderno

## Instalación

### 1. Clonar o descomprimir el repositorio

```bash
# Si has descargado el ZIP
unzip sistema_gestion_pmr.zip -d sistema_pmr
cd sistema_pmr

# O si estás clonando desde un repositorio
git clone https://tu-repositorio/sistema-pmr.git
cd sistema-pmr
```

### 2. Crear un entorno virtual (recomendado)

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

En Windows:
```bash
venv\Scripts\activate
```

En Linux/Mac:
```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Inicializar la base de datos

```bash
python init_db.py
```

## Ejecución

### Desarrollo local

```bash
python -m flask run --host=0.0.0.0
```

### Producción

```bash
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

La aplicación estará disponible en `http://localhost:5000`

## Estructura del proyecto

```
recursosweb/
├── instance/              # Base de datos SQLite
├── src/
│   ├── models/            # Modelos de datos
│   ├── routes/            # Rutas y controladores
│   ├── static/            # Archivos estáticos (JS, CSS, imágenes)
│   ├── templates/         # Plantillas HTML
│   └── main.py            # Punto de entrada principal
├── uploads/               # Directorio para archivos subidos
├── init_db.py             # Script para inicializar la base de datos
├── requirements.txt       # Dependencias del proyecto
├── requirements_prod.txt  # Dependencias para producción
└── wsgi.py                # Punto de entrada para WSGI
```

## Despliegue en servidor propio

### Opción 1: Despliegue directo

1. Instala Python 3.8+ en tu servidor
2. Sigue los pasos de instalación anteriores
3. Configura un servidor web (Nginx, Apache) como proxy inverso:

Ejemplo de configuración para Nginx:

```nginx
server {
    listen 80;
    server_name tu-dominio.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

4. Configura un servicio systemd para mantener la aplicación en ejecución:

```ini
[Unit]
Description=Sistema de Gestión de Recursos PMR
After=network.target

[Service]
User=tu-usuario
WorkingDirectory=/ruta/a/tu/aplicacion
ExecStart=/ruta/a/tu/aplicacion/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:5000 wsgi:app
Restart=always

[Install]
WantedBy=multi-user.target
```

### Opción 2: Despliegue con Docker

1. Crea un archivo `Dockerfile` en la raíz del proyecto:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python init_db.py

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
```

2. Construye y ejecuta la imagen Docker:

```bash
docker build -t sistema-pmr .
docker run -p 5000:5000 sistema-pmr
```

## Uso de PostgreSQL (opcional)

Si prefieres usar PostgreSQL en lugar de SQLite:

1. Instala PostgreSQL en tu servidor
2. Crea una base de datos y un usuario
3. Modifica la configuración en `wsgi.py`:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:contraseña@localhost/nombre_db'
```

4. Instala el driver de PostgreSQL:

```bash
pip install psycopg2-binary
```

## Soporte

Para cualquier consulta o problema, por favor contacta con el equipo de desarrollo.
