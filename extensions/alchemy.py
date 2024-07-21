from flask_sqlalchemy import SQLAlchemy
from utils.directory import get_abs_path
import os

db = SQLAlchemy()


def register_db(app):
    database = get_abs_path(os.getenv("DB_ADDR"))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    #app.config['SQLALCHEMY_ECHO'] = True
    #app.config["SQLALCHEMY_RECORD_QUERIES"] = True
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_pre_ping": True,
    }

    db.init_app(app)

    with app.app_context():
        db.create_all()
