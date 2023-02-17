

from aiogram import Router
from filters.CheckAuthorization.AuthorizationFilter import AuthorizationFilter
from aiogram.types import Message
from keyboards.ChoosingLanguage import build_languge_keyboard
from aiogram.dispatcher.filters.command import Command
from aiogram.types import CallbackQuery
from utils.UserData.authorizator import Authorizer
from utils.UserData.authorizationData import AuthorizationData
from UIStableElemenths.RegistrationConfirmation import RegistrationConfirmation,RegistrationConfirmed, RegistrationNotConfirmed
from handlers.WorkHandlers.WorkMainRouter import Say_Hello
from utils.MessageRegistrator.MessageAdder import MessageAdder

router = Router()

router.message.filter(
    AuthorizationFilter(ExpectedValue = False)
)
router.callback_query.filter(
    AuthorizationFilter(ExpectedValue = False)
)

@router.message(Command(commands = ["start"]))
async def print_language_keyboard(message: Message, UserSessionData:AuthorizationData):
    Authorizer.UpdateChatIdStatus(message.from_user.id, message.chat.id)
    MessageAdder.Add_Message(await message.answer(text="Выберите язык", reply_markup=build_languge_keyboard()), message.from_user.id)



@router.callback_query(RegistrationConfirmed.filter())
async def Authorize_User(call: CallbackQuery, UserSessionData : AuthorizationData):
    Authorizer.UpdateAuthorizationStatus(call.from_user.id, True)
    await call.answer()
    await Say_Hello(call.message, UserSessionData)

@router.callback_query(RegistrationNotConfirmed.filter())
async def User_Not_Authorized(call:CallbackQuery, UserSessionData:AuthorizationData):
    await call.answer()


@router.callback_query(lambda m:True)
async def confirming_language(call: CallbackQuery, UserSessionData:AuthorizationData):
    Authorizer.UpdateLanguage(call.from_user.id, call.data)
    await RegistrationConfirmation(call.message, AuthorizationData(Exist=False, Language=call.data))
    await call.answer()


