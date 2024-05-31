class WrongTermException(Exception):
    pass

class InvalidAliasLengthException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class InvalidDateException(Exception):
    pass