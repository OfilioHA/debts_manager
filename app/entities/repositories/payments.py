from extensions.alchemy import db
from app.entities.models import Payment


class PaymentRepository:

    def create(self, values): 
        new_payment = Payment()
        new_payment.currency_id = values['currency']
        new_payment.original = values['original']
        new_payment.debt_id = values['debt_id']
        new_payment.value = values['value']
        db.session.add(new_payment)
        db.session.commit()
        return new_payment
