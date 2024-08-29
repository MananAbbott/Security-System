import bcrypt

class KeypadAuth:
    def __init__(self, stored_hashed_password: bytes):
        """
        Initialize with a stored hashed password for authentication.
        :param stored_hashed_password: The hashed password stored securely.
        """
        self.stored_hashed_password = stored_hashed_password

    @staticmethod
    def hash_password(plain_password: str) -> bytes:
        """
        Hash a plaintext password using bcrypt.
        :param plain_password: The plaintext password to hash.
        :return: The hashed password as a byte string.
        """
        return bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())

    def verify_password(self, entered_password: str) -> bool:
        """
        Verify if the entered password matches the stored hashed password.
        :param entered_password: The password entered by the user.
        :return: True if the passwords match, False otherwise.
        """
        return bcrypt.checkpw(entered_password.encode('utf-8'), self.stored_hashed_password)
