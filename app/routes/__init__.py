from .main import main_bp
from .debtor import debtor_bp
from .debts import debt_bp

def app_register(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(debtor_bp)
    app.register_blueprint(debt_bp)


