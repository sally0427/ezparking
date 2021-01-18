from flask import Blueprint,request,jsonify
from authlib.integrations.flask_client import OAuth
from flask import Flask, redirect, url_for, session
from flask import current_app
from models import User, Car, db
from lib.jwt_utils import generate_jwt
from datetime import datetime,timedelta
from utils.commons import login_required
import random
import os
# from applet_app import oauth
# 定義藍圖路由
car_bp = Blueprint('car_bp',__name__,url_prefix='/car')

@car_bp.route('/', methods=['GET'])
#@login_required
def hello_world():
    return f"aaaaa"

@car_bp.route('/create_car', methods=['POST']) 
def create_car():
    # create_user(user_id) must be exist
    user_id = int(request.args.get("id"))
    data = dict(
        #id = 4,
        create_user = user_id, 
        car_name='aaa',
        car_license_plate = '888'
    )
    print(123456)
    car = Car(data)
    db.session.add(car)
    db.session.commit()

    ret_data={
        'msg':'添加成功',
        'car_id':car.id
    }
    return jsonify(ret_data)
    pass

@car_bp.route('/delete_car', methods=['POST'])
def delete_car():    
    search = int(request.args.get("create_user"))
    data = dict(
        create_user = search, #create_user = user_id
        car_name='bbb',
        car_license_plate = '234'
    )
    
    data = Car.query.filter_by(create_user = search).first() # create_user, use create_user to search data
    print('delete_car:', data)
    db.session.delete(data)
    db.session.commit()

    ret_data={
        'msg':'刪除成功',
        'car_id':data.id
    }
    return jsonify(ret_data)
    pass   


@car_bp.route('/find_user_car', methods=['GET'])
def find_user_car():
    # use create_user to search the users cars' information
    search = int(request.args.get("create_user"))
    objs = Car.query.filter_by(create_user = search).all()
    ret_data = []
    for obj in objs:
        car_info = {
            'car_id':obj.id,
            'create_user':obj.create_user,
            'car_name':obj.car_name,
            'car_license_plate':obj.car_license_plate
        }
        ret_data.append(car_info)
    return jsonify(ret_data)
    pass


@car_bp.route('/find_user_car_by_car_id', methods=['GET'])
def find_user_car_by_car_id():
    # use car_id to search the users cars' information 
    search = int(request.args.get("car_id"))
    obj = Car.query.filter_by(id = search).first()
    print(obj.id)
    ret_data = {
        'car_id':obj.id,
        'create_user':obj.create_user,
        'car_name':obj.car_name,
        'car_license_plate':obj.car_license_plate
    }
    return jsonify(ret_data)
    pass


@car_bp.route('/modify', methods=['POST'])
def modify():
    # choose the data and modify the information
    search = 1
    obj = Car.query.filter_by(create_user = search).first()

    obj.car_name = 'ddd'
    obj.car_license_plate = '789'
    db.session.add(obj)
    db.session.commit()

    ret_data={
        'msg':'修改成功',
        'car_id':obj.id
    }
    return jsonify(ret_data)
    pass



