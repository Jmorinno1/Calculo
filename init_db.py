import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask
from src.models.base import db

# Crear una aplicación Flask básica para inicializar la base de datos
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Importar todos los modelos para que SQLAlchemy los conozca
from src.models.aeropuerto import Aeropuerto
from src.models.asistencia import Asistencia
from src.models.parametro import Parametro
from src.models.personal import Empleado
from src.models.recurso import Recurso
from src.models.sr_historico import AsistenciaHistorica
from src.models.calculo_recurso import CalculoRecurso
from src.models.vacacion import Vacacion
from src.models.parametro_aeropuerto import ParametroAeropuerto

# Crear todas las tablas
with app.app_context():
    db.create_all()
    print("Base de datos SQLite inicializada correctamente.")
