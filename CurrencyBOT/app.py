import telebot
from config import TOKEN, keys
from extention import ConversionException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'To get started, enter the bot command in the following format:\n' \
           ' <the name of the currency you want to know the price of> <the name of the currency in which you want to find out the price of the first currency> ' \
           '<amount of first currency> \
\n view available currencies /values'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def help(message: telebot.types.Message):
    text = 'Available currencies:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) > 3:
            raise ConversionException('Incorrect input.')

        quote, base, amount = values
        total_base = CurrencyConverter.convert(quote, base, amount)

    except ConversionException as e:
        bot.send_message(message.chat.id, f'User error\n{e}')

    except Exception as e:
        bot.send_message(message.chat.id, f'Failed to process command\n{e}')

    else:
        text = f'Price {amount} {quote} in {base} = {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)