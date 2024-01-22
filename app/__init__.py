from os import path
from flask import Flask
from .views import views
from .auth import auth
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "dotabase.db"

def InitApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "rocksandstones"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Team
    
    return app