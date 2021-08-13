import jwt
from hashlib import sha256
from Auth.models import Account

secret = "qwerty!1@2#3$4malay__qwerty5782465782356934856"


def pass_hash(password):
    return sha256(password.encode()).hexdigest()


def gen_token(payload):
    return jwt.encode(payload, secret, algorithm="HS256")


def dec_token(token):
    return jwt.decode(token, secret, algorithms=["HS256"])


def valid_token(client_token):
    payload = dec_token(client_token)
    data = Account.objects.get(id=payload.id)
    if data.token == client_token and payload.email == data.email:
        return True
    return False
