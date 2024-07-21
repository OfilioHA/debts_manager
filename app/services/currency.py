from app.entities.models import Currency


class CurrencyService:

    @staticmethod
    def standardize(value, currency_id):
        if (currency_id == 1):
            return value
        currency = Currency.query.get(currency_id)
        return round(value / currency.value)
    
    @staticmethod
    def primary_currency():
        currency = Currency.query.get(1)
        return currency

                
