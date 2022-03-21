import requests
import json
from config import keys


class ConvertionException(Exception):
    pass

class Convertor:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'can not convert the same currency {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Unable to process currency {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Unable to process currency {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Unable to process quantity {amount}')


        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote_ticker}&symbols={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base

