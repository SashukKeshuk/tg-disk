from typing import Callable, Dict, Any, Awaitable
from aiogram import types
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from utils.UserData.authorizator import Authorizer
from aiogram.types import Message
from aiogram.types import CallbackQuery
from utils.MessageRegistrator.MessageAdder import MessageAdder

class AuthorizationDataMiddlewareMessage(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:

        data['UserSessionData'] = Authorizer.GetUserData(event.from_user.id)
        MessageAdder.Add_Message(event, event.from_user.id)
        ans = await handler(event, data)
        return ans

class AuthorizationDataMiddlewareCallback(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:

        data['UserSessionData'] = Authorizer.GetUserData(event.from_user.id)
        ans =  await handler(event, data)
        return ans


