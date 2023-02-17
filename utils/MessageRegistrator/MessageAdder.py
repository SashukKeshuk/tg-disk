import aiogram.types.message
from aiogram.types import Message
from utils.UserData.authorizator import Authorizer
from utils.UserData.authorizationData import AuthorizationData

class MessageAdder:

    @staticmethod
    def Add_Message(msg, user_id:int):
        if type(msg) == dict:
            Authorizer.AddNewMessage(user_id, msg["message_id"])
        if type(msg) == aiogram.types.message.Message:
            Authorizer.AddNewMessage(user_id, msg.message_id)


