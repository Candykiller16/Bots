import random

import requests
import telebot
import random
from telebot import types
import config

bot = telebot.TeleBot(config.token_for_first_bot)

BASEURL = config.BaseUrl


def get_total_confirmed_from_belarus():
    api = 'https://api.covid19api.com/summary'
    respons_from_api = requests.get(api)
    respons = respons_from_api.json()['Countries']
    for item in respons:
        if item['Country'] == 'Belarus':
            b = item['TotalConfirmed']
    return f'Общее число подтвержденных в Беларуси случаев заражения COVID-19 составляет {b}'


def get_total_confirmed_from_world():
    api = 'https://api.covid19api.com/summary'
    respons_to_totals = requests.get(api)
    respons = respons_to_totals.json()['Global']['TotalConfirmed']
    return f'Общее число подтвержденных в мире случаев заражения COVID-19 составляет {respons}'


def get_three_random_quotes():
    api = 'https://www.breakingbadapi.com/api/quotes'
    respons_from_api = requests.get(api)
    json = respons_from_api.json()
    all_quotes = [item['quote'] for item in json]
    count = 3
    three_quotes = []
    while count != 0:
        three_quotes.append(random.choice(all_quotes))
        count -= 1
    return '\n'.join(three_quotes)


def get_random_chore():
    api = 'http://www.boredapi.com/api/activity?type=diy'
    respons_from_api = requests.get(api)
    chore = respons_from_api.json()['activity']
    return chore


def get_joke():
    api = 'https://geek-jokes.sameerkumar.website/api?format=json'
    respons_from_api = requests.get(api)
    joke = respons_from_api.json()['joke']
    return joke


# @bot.message_handler(content_types='text')
# def message_reply(message):
#     if message.text == "в беларуси":
#         bot.send_message(message.chat.id, get_total_confirmed_from_belarus())
#     elif message.text == "в мире":
#         bot.send_message(message.chat.id, get_total_confirmed_from_world())
#     elif message.text == "фразы":
#         bot.send_message(message.chat.id,  get_three_random_quotes())
#     elif message.text == "мне скучно":
#         bot.send_message(message.chat.id,  get_random_chore())
#     elif message.text == "шутка":
#         bot.send_message(message.chat.id,  get_joke())

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Павiтацца")
    btn2 = types.KeyboardButton("❓ Задаць пытанне")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привiтанне, што хочаш ?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Павiтацца"):
        bot.send_message(message.chat.id, text="Прывiтанне мой дараги сябар!)")
    elif (message.text == "❓ Задаць пытанне"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        totals_in_world = types.KeyboardButton("Количество заболевших в мире")
        totals_in_belarus = types.KeyboardButton("Количество заболевших в Беларуси")
        three_quotes = types.KeyboardButton("3 фразы из Breaking Bad")
        random_chore = types.KeyboardButton("Мне скучно")
        random_joke = types.KeyboardButton("Хочу шутку")
        markup.add(totals_in_world, totals_in_belarus, three_quotes, random_chore, random_joke)
        bot.send_message(message.chat.id, text="Задаць пытанне", reply_markup=markup)
    elif (message.text == "Количество заболевших в мире"):
        bot.send_message(message.chat.id, get_total_confirmed_from_world())
    elif (message.text == "Количество заболевших в Беларуси"):
        bot.send_message(message.chat.id, get_total_confirmed_from_belarus())
    elif (message.text == "3 фразы из Breaking Bad"):
        bot.send_message(message.chat.id, get_three_random_quotes())
    elif (message.text == "Мне скучно"):
        bot.send_message(message.chat.id, get_random_chore())
    elif (message.text == "Хочу шутку"):
        bot.send_message(message.chat.id, get_joke())
    elif (message.text == "Жыве?"):
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEJpViLjvdXVRwel5ZM9RZoC3htGQYHQACBwEAAvcCyA9SzoqdIwTewyME")



# @bot.message_handler(commands=['button'])
# def button(message):
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     totals_in_world = types.InlineKeyboardButton('Количество заболевших в мире',
#                                                  callback_data='totals_in_world')
#     totals_in_belarus = types.InlineKeyboardButton('Количество заболевших в Беларуси',
#                                                    callback_data='totals_in_belarus')
#     three_quotes = types.InlineKeyboardButton('3 фразы из Breaking Bad',
#                                               callback_data='three_quotes')
#     random_chore = types.InlineKeyboardButton('Мне скучно',
#                                               callback_data='random_chore')
#     random_joke = types.InlineKeyboardButton('Хочу шутку',
#                                              callback_data='random_joke')
#     markup.add(totals_in_world, totals_in_belarus, three_quotes, random_chore, random_joke)
#
#     bot.send_message(message.chat.id, 'Привет!', reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.message:
#         if call.data == 'totals_in_world':
#             bot.send_message(call.message.chat.id, get_total_confirmed_from_world())
#         elif call.data == 'totals_in_belarus':
#             bot.send_message(call.message.chat.id, get_total_confirmed_from_belarus())
#         elif call.data == 'three_quotes':
#             bot.send_message(call.message.chat.id, get_three_random_quotes())
#         elif call.data == 'random_chore':
#             bot.send_message(call.message.chat.id, get_random_chore())
#         elif call.data == 'random_joke':
#             bot.send_message(call.message.chat.id, get_joke())


#
bot.infinity_polling()
