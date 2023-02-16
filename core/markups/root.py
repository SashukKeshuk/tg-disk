from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os

def gen_markup(uid) -> InlineKeyboardBuilder:
    #root = InlineKeyboardMarkup()
    file_list = os.listdir(f"src/{uid}")
    sorted_file_list = sorted(file_list)
    folder_markup = InlineKeyboardBuilder()
    for file in sorted_file_list:
        if (file.find('.') != -1):
            folder_markup.row(InlineKeyboardButton(text=str(file), callback_data="test"))
        else:
            folder_markup.row(InlineKeyboardButton(text=f"▸ {str(file)}", callback_data="test"))
    return folder_markup