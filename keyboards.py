import telebot
from telebot import types


def articles_keyboard(more=False):
    articles_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    da = telebot.types.KeyboardButton(text='Да')
    articles_keyboard.add(da)
    return articles_keyboard
