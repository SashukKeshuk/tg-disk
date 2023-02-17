import aiogram.types
from aiogram.utils.keyboard import InlineKeyboardBuilder

def build_languge_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(aiogram.types.InlineKeyboardButton(text = "English", callback_data = "english"))
    builder.add(aiogram.types.InlineKeyboardButton(text = "Русский", callback_data = "russian"))
    builder.adjust(2)
    return builder.as_markup()