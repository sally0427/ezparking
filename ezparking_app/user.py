from authlib.integrations.flask_client import OAuth
from flask import  redirect, url_for, session,current_app,jsonify,request,Blueprint,g
from models import User,db,Car
from sqlalchemy.exc import IntegrityError
from lib.jwt_utils import generate_jwt
from datetime import datetime,timedelta
from utils.response_code import RET
import random
from utils.commons import login_required
import os
# from applet_app import oauth
# 定義藍圖路由
user_bp = Blueprint('user_bp',__name__,url_prefix='/users')

# google login
from lib.google_utils import google,oauth

# oauth = OAuth(current_app)
# google = oauth.register(
#     name='google',
#     client_id="806521295058-l66qibahqm57lrksvtggigaq1s3o93gj.apps.googleusercontent.com",
#     client_secret="s5OwRjwwGmWWR_sgWS6OwASr",
#     access_token_url='https://accounts.google.com/o/oauth2/token',
#     access_token_params=None,
#     authorize_url='https://accounts.google.com/o/oauth2/auth',
#     authorize_params=None,
#     api_base_url='https://www.googleapis.com/oauth2/v1/',
#     userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
#     # This is only needed if using openId to fetch user info
#     client_kwargs={'scope': 'openid email profile'},
# )




@user_bp.route('/')
@login_required
def hello_world():
    email = dict(session)['user_info']['name']
    return f'Hello, you are logge in as {email}!'



@user_bp.route('/google_login')
def google_login():
    session.clear()
    if not session.get('user_info'):
        google = oauth.create_client('google')  # create the google oauth client
        redirect_uri = url_for('user_bp.authorize', _external=True)
        return google.authorize_redirect(redirect_uri)
    else:
        return redirect('/users/')


@user_bp.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    token = google.authorize_access_token()  # Access token from google (needed to get user info)
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info

    # user_info
    # {'id': '115112474685165223677', 'email': 'b10402113@gmail.com', 'verified_email': True, 'name': 'Andy Cheng',
    #  'given_name': 'Andy Cheng',
    #  'picture': 'https://lh3.googleusercontent.com/a-/AOh14GjlyqLmYj3VPyGZwvYL7pv_ALtKWfb1j_BMdw5xXQ=s96-c',
    #  'locale': 'zh-TW'}

    # user
    # {'sub': '115112474685165223677', 'name': 'Andy Cheng', 'given_name': 'Andy Cheng',
    #  'picture': 'https://lh3.googleusercontent.com/a-/AOh14GjlyqLmYj3VPyGZwvYL7pv_ALtKWfb1j_BMdw5xXQ=s96-c',
    #  'email': 'b10402113@gmail.com', 'email_verified': True, 'locale': 'zh-TW'}

    session['user_info'] = user_info
    session['user_id'] = user_info.get('id')
    user_query = User.query.filter(User.email==user_info.get('email')).first()
    if not user_query:
        db_user = User(user_info)
        try:
            db.session.add(db_user)
            db.session.commit()
        except IntegrityError as e:
            # 数据库操作错误后的回滚
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(errno=RET.DATAEXIST, errmsg="已存在")
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg="查詢異常")
    g.user_id = user_info.get('id')
    return jsonify(errno=RET.OK, errmsg="登入成功")


def _generate_jwt_token(user_id):
    # 参数：user_id表示生成token的载荷中存储用户信息
    # 步骤：
    # 1、生成当前时间
    now = datetime.utcnow()
    # 2、根据时间差，指定token的过期时间,
    # expire = now + timedelta(hours=24)
    expiry = now + timedelta(hours=current_app.config.get("JWT_EXPIRE_TIME"))
    # 3、调用jwt工具，传入过期时间
    token = generate_jwt({'user_id':user_id},expire=expiry)
    # 4、返回token
    return token


@user_bp.route("/temp_login")
def temp_login():
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    if not user:
        return jsonify(msg="用戶不存在")

    session['user_id'] = user.id
    g.user_id = user.id

    ret_data={
        'user_info':{
            'uid':user.id,
            'avatarUrl':user.avatarUrl
        }
    }
    return jsonify(ret_data)

@user_bp.route("/temp_add_car")
@login_required
def temp_add_car():

    user = User.query.filter(User.id == g.user_id).first()
    if not user:
        return jsonify(msg="用戶不存在")
    car = Car.query.filter(Car.id == 1).first()
    user.cars.append(car)
    db.session.commit()
    ret_data={
        'msg':'添加成功',
        'user_id':user.id,
        'car_id':car.id
    }
    return jsonify(ret_data)





@user_bp.route("/temp_add_user",methods=['GET'])
def temp_add_user():
    random_num = random.randint(0,10000000)

    data = dict(
        openId = random_num,
        email='aaaass@gmail.com',
        avatarUrl = 'default',
        id =3,
        name='andasdyq2'
    )
    user = User(data)
    db.session.add(user)
    db.session.commit()


    ret_data={
        'msg':'添加成功',
        'user_id':user.id
    }
    return jsonify(ret_data)
    pass

