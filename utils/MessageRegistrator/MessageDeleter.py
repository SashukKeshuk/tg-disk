from aiogram.types import Message
from utils.UserData.authorizator import Authorizer
from utils.UserData.authorizationData import AuthorizationData

class MessageAdder:

    @staticmethod
    def Add_Message(msg:Message, user_id:int):
        Authorizer.DeleteLastMessage(user_id)
