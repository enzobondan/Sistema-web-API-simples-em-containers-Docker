from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .routes import init_app
    init_app(app)
    
    try:
        with app.app_context():
            db.create_all()
    except Exception as e:
        app.logger.error(f"Failed to create database tables: {str(e)}")
    
    return app