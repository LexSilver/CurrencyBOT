import telebot
from config import TOKEN, keys
from extensions import ConvertionException, Convertor

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
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
    base, sym, amount = message.text.split(' ')
    r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote_ticker}&symbols={base_ticker}')
    resp = json.loads(r.content)
    new_price = resp['rates'][sym] * float(amount)
    bot.reply_to(message, f"Цена {amount} {base} в {sym} : {new_price}")

bot.polling()