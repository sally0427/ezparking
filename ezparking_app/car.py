from flask import Blueprint,request,jsonify
from authlib.integrations.flask_client import OAuth
from flask import Flask, redirect, url_for, session
from flask import current_app
from models import User,db,Car
from lib.jwt_utils import generate_jwt
from datetime import datetime,timedelta
import random
import os
# from applet_app import oauth
# 定義藍圖路由
car_bp = Blueprint('car_bp',__name__,url_prefix='/car')

@car_bp.route('/')
def hello_world():
    car = Car.query.filter(Car.id == 1).first()
    print(car.user)
    return f"car bp"



@car_bp.route('/add_car',methods=['GET'])
def add_car():
    new_car = Car()
    new_car.car_license_plate="123"
    new_car.car_name="123"
    new_car.create_user=2
    # new_car.belong_user = 2
    # new_car.cr
    db.session.add(new_car)

    db.session.commit()
    msg = {
        "msg":"ok",
    }
    return jsonify(msg)