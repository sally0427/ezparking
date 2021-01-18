import jwt
from flask import current_app

def generate_jwt(payload,expire,secret_key=None):
    _payload = {'exp':expire}
    _payload.update(payload)
    if not secret_key:
        secret_key = current_app.config['SECRET_KEY']
    token = jwt.encode(_payload,secret_key,algorithm='HS256')
    return token.decode()


def verify_jwt(token, secret_key=None):
    if not secret_key:
        secret_key = current_app.config.get('SECRET_KEY')
    try:
        payload = jwt.decode(token,secret_key,algorithms=['HS256'])
    except jwt.PyJWTError:
        payload = None
    return payload

