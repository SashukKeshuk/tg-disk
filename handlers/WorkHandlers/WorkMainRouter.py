
from aiogram import Router
from aiogram.types import Message
from utils.UserData.authorizationData import AuthorizationData
from filters.CheckAuthorization.AuthorizationFilter import AuthorizationFilter
from utils.MessageRegistrator.MessageAdder import MessageAdder

router = Router()
router.message.filter(
    AuthorizationFilter(ExpectedValue = True)
)
router.callback_query.filter(
    AuthorizationFilter(ExpectedValue = True)
)

@router.message(lambda m:True)
async def Say_Hello(mess:Message, UserSessionData:AuthorizationData):
    MessageAdder.Add_Message(await  mess.answer("Ку"), mess.from_user.id)