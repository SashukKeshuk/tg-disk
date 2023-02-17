from .authorizationData import AuthorizationData

users_data = {}

class Authorizer:
    @staticmethod
    def GetUserData(id : int) -> AuthorizationData:
        if (id in users_data):
            return users_data[id]
        else:
            return AuthorizationData()

    @staticmethod
    def UpdateLanguage(id:int, Language:str):
        if (id in users_data):
            data = users_data[id]
            data.Language = Language
            users_data[id] = data
        else:
            users_data[id] = AuthorizationData(Language=Language)

    @staticmethod
    def UpdateChatIdStatus(id:int, ChatId:int):
        if (id in users_data):
            print(ChatId)
            data = users_data[id]
            data.ChatId = ChatId
            users_data[id] = data
        else:
            users_data[id] = AuthorizationData(ChatId=ChatId)
    @staticmethod
    def UpdateAuthorizationStatus(id:int, Exist:bool):
        if not Exist:
            users_data[id] = AuthorizationData()
        else:
            if (id in users_data):
                data = users_data[id]
                data.Exist = Exist
                users_data[id] = data
            else:
                users_data[id] = AuthorizationData(Exist=Exist)

    @staticmethod
    def AddNewMessage(user_id:int, message_id:int):
        if (user_id not in users_data):
            users_data[id] = AuthorizationData()
        data = users_data[id]
        data.MessageIds.append(message_id)
        users_data[id] = data

    @staticmethod
    def DeleteLastMessage(user_id : int):
        if (id in users_data):
            data = users_data[id]
            if (data.MessageIds.length() > 0):
                data.pop(-1)
            users_data[id] = data