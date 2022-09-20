from passlib.hash import bcrypt
from Crypto.Cipher import AES
from Crypto import Random

from config.settings import Settings

settings = Settings()
BS = 16
pad= lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad= lambda s: s[:-ord(s[len(s) - 1:])]


def create_hash(password: str):
    return bcrypt.hash(password)


def verify_hash(plain_password: str,
                hashed_password: str):
    return bcrypt.verify(plain_password,
                         hashed_password)


def encrypt(raw):
    raw = pad(raw).encode()
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(settings.SECRET_KEY.encode(), AES.MODE_CBC, iv)
    return (iv + cipher.encrypt(raw)).hex()


def decrypt(enc: str):
    enc = bytes.fromhex(enc)
    iv = enc[:16]
    cipher = AES.new(settings.SECRET_KEY.encode(), AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]).decode())
