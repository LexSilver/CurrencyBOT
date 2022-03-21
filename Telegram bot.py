# import telebot
#
# TOKEN = "5163414766:AAEJCIPJCSkqb6aZRJtgQK6COkKygMoDqYc"
#
# bot = telebot.TeleBot(TOKEN)
#
#
# # Обрабатываются все сообщения содержащие команды '/start' or '/help'.
# @bot.message_handler(commands=['start', 'help'])
# def handle_start_help(message):
#     bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")
#     bot.reply_to(message, "Need help?")
#
#
#
# # Обрабатывается все документы и аудиозаписи
# @bot.message_handler(content_types=['voice', 'audio'])
# def handle_docs_audio(audio):
#     bot.reply_to(audio, "Beautiful voice")
#
# # на сообщения с фотографией будет отвечать сообщением «Nice meme XDD
# @bot.message_handler(content_types=['photo'])
# def handle_photo(photo):
#     bot.reply_to(photo, "«Nice meme XDD»")
#
#
#
# bot.polling(none_stop=True)



import telebot
import requests
import json



TOKEN = '5221689334:AAGQqmg7S4X3wqL4caLrXF3oXKuYpdAwV9w'


bot = telebot.TeleBot(TOKEN)

keys = {
    "Bitcoin": "BTC",
    "Etherium": "ETH",
    "Dollar": "USD"
}

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quite: str, base: str, amount: str):
        if quite == base:
            raise ConvertionException(f'can not convert the same currency {base}.')


@bot.message_handler(commands=('start', 'help'))
def help(message: telebot.types.Message):
    text = 'To get started, enter a request in the format: \n<currency name> \
<what currency to convert> \
<amount of convertible currency> \n To see all visible currency enter: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Available currencies'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')

    if len(values) > 3:
        raise ConvertionException('Too many parameters')

    quote, base, amount = values

    if quote == base:
        raise ConvertionException(f'can not convert the same currency {base}. ')

    try:
        quote_ticker = keys[quote]
    except KeyError:
        raise ConvertionException(f'Unable to process currency {quote}')

    try:
        base_ticker = keys[base]
    except KeyError:
        raise ConvertionException(f'Unable to process currency {base}')

    try:
        amount = float[amount]
    except ValueError:
        raise ConvertionException(f'Unable to process quantity {amount}')

    quote_ticker, base_ticker = keys[quote], keys[base]
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
    total_base = json.loads(r.content)[keys[base]]
    text = f'price {amount} {quote} in {base} - {total_base}'
    bot.send_message(message.chat.id, text)


@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hello')

bot.polling()