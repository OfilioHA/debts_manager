from app.forms.DebtorForm import DebtorForm
from app.entities.models import Debt, Debtor, Currency
from app.entities.repositories import DebtRepository


class DebtService:

    repository: DebtRepository

    def __init__(self):
        self.repository = DebtRepository()

    def get_debtors_debts(self, debtors: list[Debtor]):
        debtors_list = []

        for debtor in debtors:
            value = {}
            value['id'] = debtor.id
            value['name'] = debtor.name
            value['debt'] = self.get_current_debt(debtor)
            debtors_list.append(value)

        return debtors_list

    def get_current_debt(self, debtor: Debtor):
        debt = self.repository.get_current_debt(debtor.id)
        return debt if debt else 0

    def create_debt(self, values):
        debt = self.repository.create(values)
        return debt
