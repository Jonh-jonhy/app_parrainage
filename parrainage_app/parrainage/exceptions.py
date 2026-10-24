from .models import Parrain
class ParrainageError(Exception):...

class ParrainExistantError(ParrainageError):
    def __init__(message:str, Parrain:Parrain):
        return f"{message}"