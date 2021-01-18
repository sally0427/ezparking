
from flask import request,g
from .jwt_utils import verify_jwt
"""

"""
# @app.before_request
def before_request():
    auth = request.headers.get('Authorization')
    if auth:
        # 使用jwt工具校驗
        payload = verify_jwt(token=auth)
        if payload:
            g.user_id = payload.get("user_id")
        pass