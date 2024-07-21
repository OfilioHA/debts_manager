from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class DebtorForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    submit = SubmitField('Guardar')
