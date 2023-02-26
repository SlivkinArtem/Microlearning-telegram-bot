# import config
import os
import time

import telebot

import keyboards
import random_function

name = ''

bot = telebot.TeleBot('тут должен быть токен')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Привет, {message.from_user.first_name}, я телеграмм-бот по микрообучению. '
                          f'Я буду скидыват вам факты и статьи по астрономии каждый день. Давайте сразу начнём')
    current_parser = random_function.get_random_parser()
    bot.send_message(message.chat.id, 'Подбираю контент для вас, подождите')
    current_parser()
    time.sleep(5)

    if current_parser.__name__ == 'parse_hubble':
        with open('hubble/article_text.txt') as txt:
            data = txt.read()
            if len(data) < 4096:
                bot.send_message(message.chat.id, data)
            else:
                for x in range(0, len(data), 4096):
                    bot.send_message(message.chat.id, '{}'.format(data[x:x + 4096]))

        for file in os.listdir('hubble/pictures'):
            with open(f'hubble/pictures/{file}', 'rb') as pic:
                bot.send_photo(message.chat.id, pic)

        for file in os.listdir('hubble/pictures'):
            os.remove(f'hubble/pictures/{file}')

    elif current_parser.__name__ == 'parse_100_facts':
        bot.send_message(message.chat.id, current_parser())

    else:
        with open('indicator/article_text.txt') as txt:
            data = txt.read()
            if len(data) < 4096:
                bot.send_message(message.chat.id, data)
            else:
                for x in range(0, len(data), 4096):
                    bot.send_message(message.chat.id, '{}'.format(data[x:x + 4096]))

        for file in os.listdir('indicator/pictures'):
            with open(f'indicator/pictures/{file}', 'rb') as pic:
                bot.send_photo(message.chat.id, pic)

        for file in os.listdir('indicator/pictures'):
            os.remove(f'indicator/pictures/{file}')

    bot.send_message(message.chat.id, text='Хотите получить ещё одну статью или факт?',
                     reply_markup=keyboards.articles_keyboard())


@bot.message_handler(content_types=['text'])
def buttons(message):
    if message.text.lower() == 'да':
        current_parser = random_function.get_random_parser()
        bot.send_message(message.chat.id, 'Подбираю контент для вас, подождите')
        current_parser()
        time.sleep(5)

        if current_parser.__name__ == 'parse_hubble':
            with open('hubble/article_text.txt') as txt:
                data = txt.read()
                if len(data) < 4096:
                    bot.send_message(message.chat.id, data)
                else:
                    for x in range(0, len(data), 4096):
                        bot.send_message(message.chat.id, '{}'.format(data[x:x + 4096]))

            for file in os.listdir('hubble/pictures'):
                with open(f'hubble/pictures/{file}', 'rb') as pic:
                    bot.send_photo(message.chat.id, pic)

            for file in os.listdir('hubble/pictures'):
                os.remove(f'hubble/pictures/{file}')

        elif current_parser.__name__ == 'parse_100_facts':
            bot.send_message(message.chat.id, current_parser())

        else:
            with open('indicator/article_text.txt') as txt:
                data = txt.read()
                if len(data) < 4096:
                    bot.send_message(message.chat.id, data)
                else:
                    for x in range(0, len(data), 4096):
                        bot.send_message(message.chat.id, '{}'.format(data[x:x + 4096]))

            for file in os.listdir('indicator/pictures'):
                with open(f'indicator/pictures/{file}', 'rb') as pic:
                    bot.send_photo(message.chat.id, pic)

            for file in os.listdir('indicator/pictures'):
                os.remove(f'indicator/pictures/{file}')

        bot.send_message(message.chat.id, text='Хотите получить ещё одну статью или факт?',
                         reply_markup=keyboards.articles_keyboard())


# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == "responce":
#         msg = 'статья'
#         bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True)
