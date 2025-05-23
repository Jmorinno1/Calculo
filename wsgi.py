from flask import Flask, render_template
import os
from src.models.base import db
from src.routes.parametros import parametros_bp
from src.routes.personal import personal_bp
from src.routes.asistencias import asistencias_bp
from src.routes.calculos import calculos_bp
from src.routes.importacion import importacion_bp
from src.routes.visualizacion import visualizacion_bp
from src.routes.aeropuertos import aeropuertos_bp
from src.routes.recursos import recursos_bp
from src.routes.sr_historico import sr_historico_bp
from src.routes.parametros_aeropuerto import parametros_aeropuerto_bp
from src.routes.vacaciones import vacaciones_bp

def create_app():
    """Crear y configurar la aplicación Flask"""
    app = Flask(__name__, 
                static_folder='src/static',
                static_url_path='/static',
                template_folder='src/templates')
    
    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recursos_pmr.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar extensiones
    db.init_app(app)
    
    # Registrar blueprints
    app.register_blueprint(parametros_bp)
    app.register_blueprint(personal_bp)
    app.register_blueprint(asistencias_bp)
    app.register_blueprint(calculos_bp)
    app.register_blueprint(importacion_bp)
    app.register_blueprint(visualizacion_bp)
    app.register_blueprint(aeropuertos_bp)
    app.register_blueprint(recursos_bp)
    app.register_blueprint(sr_historico_bp)
    app.register_blueprint(parametros_aeropuerto_bp)
    app.register_blueprint(vacaciones_bp)
    
    # Crear base de datos si no existe
    with app.app_context():
        db.create_all()
    
    # Ruta principal
    @app.route('/')
    def index():
        return app.send_static_file('index.html')
    
    # Ruta para el diseño mixto
    @app.route('/diseno-mixto')
    def diseno_mixto():
        """Mostrar la página del diseño mixto"""
        return render_template('diseno_mixto.html')
    
    return app

# Crear aplicación Flask
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
