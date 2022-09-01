from passlib.hash import bcrypt


def create_hash(password: str):
    return bcrypt.hash(password)


def verify_hash(plain_password: str,
                hashed_password: str):
    return bcrypt.verify(plain_password,
                         hashed_password)

