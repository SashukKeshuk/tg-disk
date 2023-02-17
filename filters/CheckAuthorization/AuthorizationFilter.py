from aiogram.dispatcher.filters import BaseFilter
from utils.UserData.authorizationData import AuthorizationData
from aiogram.types import Message

class AuthorizationFilter(BaseFilter):
    ExpectedValue : bool

    async def __call__(self, ms : Message, UserSessionData:AuthorizationData) -> bool:
        return UserSessionData.Exist == self.ExpectedValue