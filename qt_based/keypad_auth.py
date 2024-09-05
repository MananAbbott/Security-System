import bcrypt

class KeypadAuth:
    def __init__(self, stored_hashed_password: bytes):
        self.stored_hashed_password = stored_hashed_password

    @staticmethod
    def hash_password(plain_password: str) -> bytes:
        return bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())

    def verify_password(self, entered_password: str) -> bool:
        return bcrypt.checkpw(entered_password.encode('utf-8'), self.stored_hashed_password)