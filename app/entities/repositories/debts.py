from extensions.alchemy import db
from sqlalchemy.sql import functions
from app.entities.models import Debt


class DebtRepository:

    def create(self, values):
        new_debt = Debt()
        new_debt.concept = values['concept']
        new_debt.interest = values['interest']
        new_debt.value = values['value']
        new_debt.debtor_id = values['debtor']
        db.session.add(new_debt)
        db.session.commit()
        return new_debt

    def get_current_debt(self, debtor_id):
        query = db.session \
            .query(functions.sum(Debt.value).label('current_debt')) \
            .filter(Debt.debtor_id == debtor_id)
        return query.scalar()
