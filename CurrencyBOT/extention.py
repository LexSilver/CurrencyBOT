import requests
import json
from config import keys

class ConversionException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConversionException(f'Unable to transfer identical currencies {base} = {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'{quote} - Unable to process currency')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'{base} - Unable to process currency')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Unable to process currency {amount}')

        if float(amount) <= 0:
            raise ConversionException('The number must be greater than 0.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = round(json.loads(r.content)[keys[base]] * float(amount), 2)

        return total_base