from extensions.alchemy import db
from app.entities.mixins import TimeStampMixin


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12))
    symbol = db.Column(db.String(5))
    value = db.Column(db.Float)


class Debtor(db.Model, TimeStampMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Debt(db.Model, TimeStampMixin):
    id = db.Column(db.Integer, primary_key=True)
    debtor_id = db.Column(db.Integer, db.ForeignKey(Debtor.id), nullable=False)
    concept = db.Column(db.String)
    interest = db.Column(db.Integer)
    value = db.Column(db.Float)


class Payment(db.Model, TimeStampMixin):
    id = db.Column(db.Integer, primary_key=True)
    currency_id = db.Column(
        db.Integer, db.ForeignKey(Currency.id), nullable=False)
    debt_id = db.Column(db.Integer, db.ForeignKey(Debt.id), nullable=False)
    value = db.Column(db.Float)
    origin_value = db.Column(db.Float)
