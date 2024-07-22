from app.entities.models import Debt, Debtor, Currency
from app.entities.repositories import DebtRepository, PaymentRepository
from .currency import CurrencyService


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

    def standardize_value(self, values):
        value = float(values['value'])
        currency = values['currency']
        values["value"] = CurrencyService.standardize(value, currency)

    def get_current_debt(self, debtor: Debtor):
        debt = self.repository.get_current_debt(debtor.id)
        return debt if debt else 0

    def create_debt(self, values):
        debt = self.repository.create(values)
        return debt

    def edit_debt(self, debt: Debt, values):
        debt = self.repository.edit(debt, values)
        return debt

    def form_feed_choices(self, form):
        currencies = [
            (currency.id, currency.name)
            for currency
            in Currency.query.all()
        ]
        form.set_currencies(currencies)

    def save_payment(self, values, debt: Debt):
        repository = PaymentRepository()
        values['debt_id'] = debt.id
        repository.create(values)

    def save_original_value(self, values):
        values['original'] = values['value']
