from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from utils.UserData.authorizationData import AuthorizationData
from aiogram.types import Message
from aiogram.dispatcher.filters.callback_data import CallbackData
from typing import Optional
from utils.MessageRegistrator.MessageAdder import MessageAdder

from aiogram.types import CallbackQuery

class RegistrationConfirmed(CallbackData, prefix="RegistrationConfirmed"):
    o : Optional[int]



class RegistrationNotConfirmed(CallbackData, prefix="RegistrationNotConfirmed"):
    o : Optional[int]



dc = {
    "english" : ["Do you really want to continue with this settings?", "Yes"],
    "russian" : ["Хотите продолжить с выбранными настройками?", "Да"]
}

async def RegistrationConfirmation(ms: Message, data : AuthorizationData):
    kb = InlineKeyboardBuilder()
    kb.button(text=dc[data.Language][1], callback_data=RegistrationConfirmed())
#    kb.button(text=dc[data.Language][2], callback_data=RegistrationNotConfirmed())
    MessageAdder.Add_Message(await ms.answer(text=dc[data.Language][0], reply_markup=kb.as_markup()), ms.from_user.id)



