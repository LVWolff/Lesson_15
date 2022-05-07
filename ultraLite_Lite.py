

import telebot

TOKEN = '5227287892:AAHstiJj987EHuyVBwGpxWnFiR_fM0Ruzxs'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def command_start_function(message):
    bot.reply_to(message, 'Рад вас приветствовать!')

@bot.message_handler(commands = ['help'])
def command_start_function(message):
    bot.reply_to(message, 'Чем могу Вам помочь?')

@bot.message_handler(commands=['admin'])
def admin_(message):
    if message.from_user.id == 312828926:
        bot.reply_to(message, 'Слушаюсь и повинуюсь мой хозяин!')
    else:
        bot.reply_to(message, 'У вас нет доступа к администрированию!')

@bot.message_handler(content_types=['text'])
def recive_text(message):
    text = message.text
    answer_text = ''

    if text == 'Привет':
        answer_text = "Добрый день! Рад вас приветствовать!"
    elif text == 'Как дела?':
        answer_text = "Отлично! А у Вас?"
    elif text == 'Какая погода?':
        answer_text = "Отличная погода!"
    else:
        answer_text = "Моя твоя не понимать :("

    bot.reply_to(message, answer_text)

bot.polling()