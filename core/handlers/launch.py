from aiogram import Router
from aiogram.dispatcher.filters.text import Text
from aiogram.types import Message, CallbackQuery
from markups.start import start_markup
from markups.root import gen_markup

router = Router()

@router.message(commands=["start"])
async def cmd_start(msg: Message):
    await msg.answer(f"Здравствуйте, {msg.from_user.username}!", reply_markup=start_markup.as_markup())

@router.callback_query(text='start')
async def start(clb: CallbackQuery):
    await clb.message.answer(f"Ваша корневая директория", reply_markup=gen_markup(clb.from_user.id).as_markup())