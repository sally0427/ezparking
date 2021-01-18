from flask import Flask
from authlib.integrations.flask_client import OAuth
import os
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.INFO)

file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)

formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')

file_log_handler.setFormatter(formatter)

logging.getLogger().addHandler(file_log_handler)

logging.basicConfig(level=logging.INFO)

file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)

formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')

file_log_handler.setFormatter(formatter)

logging.getLogger().addHandler(file_log_handler)

# 定義工廠函數
def create_app(config_name=None):
    app = Flask(__name__)
    app.config.from_object(config_name)

    # oauth = OAuth(app)
    # google = oauth.register(
    #     name='google',
    #     client_id=os.getenv("806521295058-l66qibahqm57lrksvtggigaq1s3o93gj.apps.googleusercontent.com"),
    #     client_secret=os.getenv("s5OwRjwwGmWWR_sgWS6OwASr"),
    #     access_token_url='https://accounts.google.com/o/oauth2/token',
    #     access_token_params=None,
    #     authorize_url='https://accounts.google.com/o/oauth2/auth',
    #     authorize_params=None,
    #     api_base_url='https://www.googleapis.com/oauth2/v1/',
    #     userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    #     # This is only needed if using openId to fetch user info
    #     client_kwargs={'scope': 'openid email profile'},
    # )
    # print(oauth)
    # 導入藍圖
    from .user import user_bp
    app.register_blueprint(user_bp)
    from .car import car_bp
    app.register_blueprint(car_bp)
    from .order import order_bp
    app.register_blueprint(order_bp)
    from models import db
    db.init_app(app)



    # 導入請求鉤子
    from lib.middleware import before_request
    # 相當於裝飾器調用
    app.before_request(before_request)

    return app


