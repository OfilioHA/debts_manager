from app.entities.models import Currency
import os


class CurrencyService:

    @staticmethod
    def standardize(value, currency_id):
        currency_main_id = os.getenv("CURRENCY_MAIN")
        if (currency_id == currency_main_id):
            return value
        currency = Currency.query.get(currency_id)
        return round(value / currency.value)

    @staticmethod
    def primary_currency():
        currency_id = os.getenv("CURRENCY_MAIN")
        currency = Currency.query.get(currency_id)
        return currency
