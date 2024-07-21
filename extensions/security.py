import os
from app.forms.LoginForm import LoginForm
from app.entities.models import User, Role
from flask_security import Security, SQLAlchemyUserDatastore, SQLAlchemyUserDatastore, hash_password
from extensions.alchemy import db

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(datastore=user_datastore, login_form=LoginForm)


def register_security(app):
    app.config["REMEMBER_COOKIE_SAMESITE"] = "strict"
    app.config["SESSION_COOKIE_SAMESITE"] = "strict"
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
    app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT")
    app.config['SECURITY_URL_PREFIX'] = None
    app.config['SECURITY_LOGIN_URL'] = '/login'
    security.init_app(app)

    with app.app_context():
        if not security.datastore.find_user(email="test@me.com"):
            security.datastore.create_user(
                email="test@me.com",
                password=hash_password("password"),
                username="admin"
            )
            db.session.commit()
