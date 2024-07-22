from wtforms import SelectField, FloatField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class PaymentCreateForm(FlaskForm):

    def set_currencies(self, currencies):
        self.currency.choices = currencies

    currency = SelectField('Moneda', validators=[DataRequired()])
    value = FloatField('Cantidad', validators=[DataRequired()])
    submit = SubmitField('Registrar')
