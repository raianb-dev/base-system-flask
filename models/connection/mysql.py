from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import  JWTManager
from flask_migrate import Migrate
from datetime import timedelta

def connection_mysql():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '932bb014dbbd47f7aff1d4a381ff486b'
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    jwt = JWTManager(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/database'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    return db, app


