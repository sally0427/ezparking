from werkzeug.routing import BaseConverter
from flask import session, jsonify, g
from .response_code import RET
import functools


# 登錄狀態裝飾器
def login_required(view_func):

    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):
        user_id = session.get("user_id")

        if user_id is not None:
            g.user_id = user_id
            return view_func(*args, **kwargs)
        else:
            # 如果未登录，返回未登录的信息
            return jsonify(errno=RET.SESSIONERR, errmsg="未登錄")

    return wrapper




# @login_required
# def set_user_avatar():
#     # user_id = session.get("user_id")
#     user_id = g.user_id
#     return json  ""
#
#
# set_user_avatar()  -> wrapper()