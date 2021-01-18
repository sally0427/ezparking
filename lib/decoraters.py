
from flask import g,jsonify
import functools

def login_required(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        if not g.user_id:
            return jsonify(msg='token error'), 401
        return func(*args,**kwargs)
    return wrapper