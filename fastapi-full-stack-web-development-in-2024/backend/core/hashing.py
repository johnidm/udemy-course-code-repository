from passlib.context import CryptContext


__context = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"])


def verify_password(plain_password, hashed_password):
    return __context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return __context.hash(password)
