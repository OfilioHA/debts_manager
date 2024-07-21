from flask_wtf.form import _Auto
from wtforms import StringField, SubmitField, SelectField, FloatField, IntegerField, HiddenField
from wtforms.validators import DataRequired, NumberRange, InputRequired
from flask_wtf import FlaskForm


class DebtForm(FlaskForm):

    def set_currencies(self, currencies):
        self.currency.choices = currencies

    debtor = HiddenField('Deudor', validators=[DataRequired()])
    concept = StringField('Concepto', validators=[DataRequired()])
    currency = SelectField('Moneda', validators=[DataRequired()])
    interest = IntegerField('Interes', validators=[InputRequired(), NumberRange(0,100)])
    value = FloatField('Cantidad', validators=[DataRequired()])
    submit = SubmitField('Guardar')