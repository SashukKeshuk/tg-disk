from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

b1 = InlineKeyboardButton(text='Зайти в директорию', callback_data='start')
start_markup = InlineKeyboardBuilder()
start_markup.add(b1)