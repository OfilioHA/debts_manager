from flask import Flask
from app.routes import app_register
from app.entities.models import *
from extensions.alchemy import register_db
from extensions.security import register_security
import dotenv
import os
dotenv.load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = eval(os.getenv("MODE_DEBUG"))


@app.context_processor
def inject_user():
    from flask_login import current_user
    from flask import request
    
    url_prefix = request.path.split("/")[1]

    return dict(
        current_user=current_user,
        actual_route=request.path,
        url_prefix=url_prefix
    )


register_db(app)
register_security(app)
app_register(app)
