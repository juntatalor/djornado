import binascii
import hashlib

from project.config.settings import secret_key


def make_password(word):
    dk = hashlib.pbkdf2_hmac('sha256', word.encode(), secret_key.encode(), 100000)
    return binascii.hexlify(dk)


def check_password(word, password):
    return make_password(word) == password