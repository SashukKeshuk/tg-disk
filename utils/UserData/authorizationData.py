
class AuthorizationData:



    def __init__(self, Exist:bool = False, Language:str = "english", MessageIds = list(), ChatId:int = 0):
        self.Exist = Exist
        self.Language = Language
        self.MessageIds = MessageIds
        self.ChatId = ChatId
